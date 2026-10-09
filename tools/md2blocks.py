#!/usr/bin/env python3
"""md2blocks - parse the Frontline source markdown into structured blocks.

No external dependencies. Produces a block list suitable for rendering to HTML,
plus a coverage report so fidelity can be *proven* rather than asserted.
"""
import json
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------- punctuation
DASHES = {"\u2014": ", ", "\u2013": ", ", "\u2012": ", "}


def norm(text: str) -> str:
    """Normalise the banned dash family without losing meaning."""
    for bad, good in DASHES.items():
        text = text.replace(f" {bad} ", good).replace(bad, good)
    text = re.sub(r",\s*,", ",", text)
    text = re.sub(r"\s+,", ",", text)
    text = re.sub(r"\(\s*,\s*", "(", text)
    text = re.sub(r",\s*\)", ")", text)
    text = re.sub(r" {2,}", " ", text)
    return text.strip()


INLINE_RE = re.compile(
    r"(?P<code>`[^`]+`)"
    r"|(?P<link>\[[^\]]+\]\([^)]+\))"
    r"|(?P<bold>\*\*[^*]+\*\*)"
    r"|(?P<ital>\*[^*\n]+\*)"
)


def inline(text: str) -> str:
    """Escape then re-apply the small inline subset the sources use."""
    out, last = [], 0
    for m in INLINE_RE.finditer(text):
        out.append(esc(text[last:m.start()]))
        raw = m.group(0)
        if m.lastgroup == "code":
            out.append(f"<code>{esc(raw[1:-1])}</code>")
        elif m.lastgroup == "link":
            label, url = re.match(r"\[([^\]]+)\]\(([^)]+)\)", raw).groups()
            # No href: an unlinked citation keeps the information without
            # creating a fetchable external reference.
            out.append(f'<span class="cite">{esc(label)}<span class="cite-url">{esc(url)}</span></span>')
        elif m.lastgroup == "bold":
            out.append(f"<strong>{inline(raw[2:-2])}</strong>")
        else:
            out.append(f"<em>{inline(raw[1:-1])}</em>")
        last = m.end()
    out.append(esc(text[last:]))
    return "".join(out)


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def slug(s: str) -> str:
    s = re.sub(r"<[^>]+>", "", s)
    s = s.lower()
    s = re.sub(r"[^a-z0-9\u3040-\u30ff\u4e00-\u9fff]+", "-", s).strip("-")
    return s or "section"


def is_table_sep(line: str) -> bool:
    return bool(re.match(r"^\|[\s:\-|]+\|\s*$", line))


def split_row(line: str):
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [c.strip() for c in line.split("|")]


def parse(text: str):
    lines = text.split("\n")
    # A leading YAML frontmatter block is machine metadata on the source skill
    # files, not reference content: skip it rather than rendering it as prose.
    if lines and lines[0].strip() == "---":
        for j in range(1, len(lines)):
            if lines[j].strip() == "---":
                lines = lines[j + 1:]
                break
    blocks, i, n = [], 0, len(lines)
    stats = {"heading": 0, "table": 0, "tablerow": 0, "bullet": 0, "code": 0, "quote": 0, "para": 0}
    pending_list = None

    def flush_list():
        nonlocal pending_list
        if pending_list:
            blocks.append(pending_list)
            pending_list = None

    while i < n:
        raw = lines[i]
        line = raw.rstrip()
        stripped = line.strip()

        # raw anchor lines from the sources
        m = re.match(r'^<a\s+id="([^"]+)"></a>\s*$', stripped)
        if m:
            flush_list()
            blocks.append({"type": "anchor", "id": m.group(1)})
            i += 1
            continue

        if not stripped:
            flush_list()
            i += 1
            continue

        # fenced code
        if stripped.startswith("```"):
            flush_list()
            lang = stripped[3:].strip()
            body, i = [], i + 1
            while i < n and not lines[i].strip().startswith("```"):
                body.append(lines[i])
                i += 1
            i += 1
            blocks.append({"type": "code", "lang": lang, "text": "\n".join(body)})
            stats["code"] += 1
            continue

        # heading
        m = re.match(r"^(#{1,6})\s+(.*)$", stripped)
        if m:
            flush_list()
            level, txt = len(m.group(1)), norm(m.group(2))
            blocks.append({"type": "heading", "level": level, "html": inline(txt),
                           "text": re.sub(r"<[^>]+>", "", txt), "id": slug(txt)})
            stats["heading"] += 1
            i += 1
            continue

        # table
        if stripped.startswith("|") and i + 1 < n and is_table_sep(lines[i + 1].strip()):
            flush_list()
            head = [norm(c) for c in split_row(stripped)]
            i += 2
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                rows.append([norm(c) for c in split_row(lines[i].strip())])
                i += 1
            blocks.append({"type": "table", "head": head, "rows": rows})
            stats["table"] += 1
            stats["tablerow"] += len(rows)
            continue

        # blockquote
        if stripped.startswith(">"):
            flush_list()
            body = []
            while i < n and lines[i].strip().startswith(">"):
                body.append(lines[i].strip().lstrip(">").strip())
                i += 1
            blocks.append({"type": "quote", "html": inline(norm(" ".join(body)))})
            stats["quote"] += 1
            continue

        # horizontal rule
        if re.match(r"^([-*_])\1{2,}$", stripped):
            flush_list()
            blocks.append({"type": "rule"})
            i += 1
            continue

        # list (one nesting level)
        m = re.match(r"^(\s*)([-*+]|\d+[.)])\s+(.*)$", line)
        if m:
            indent, marker, txt = len(m.group(1)), m.group(2), m.group(3)
            kind = "ol" if marker[0].isdigit() else "ul"
            if pending_list is None or pending_list["kind"] != kind or pending_list["depth"] != (indent >= 2):
                flush_list()
                pending_list = {"type": "list", "kind": kind, "depth": indent >= 2, "items": []}
            item = {"html": inline(norm(txt))}
            # absorb continuation lines
            j = i + 1
            while j < n and lines[j].strip() and not re.match(r"^(\s*)([-*+]|\d+[.)])\s+", lines[j]) \
                    and not re.match(r"^(#{1,6}\s|\||>|```)", lines[j].strip()):
                item["html"] += " " + inline(norm(lines[j].strip()))
                j += 1
            pending_list["items"].append(item)
            stats["bullet"] += 1
            i = j
            continue

        # paragraph
        flush_list()
        body = [stripped]
        i += 1
        while i < n and lines[i].strip() and not re.match(
                r"^(\s*)([-*+]|\d+[.)])\s+|^#{1,6}\s|\||^>|^```|^<a\s+id=", lines[i]):
            body.append(lines[i].strip())
            i += 1
        blocks.append({"type": "para", "html": inline(norm(" ".join(body)))})
        stats["para"] += 1

    flush_list()
    return blocks, stats


def build(paths):
    out, report = [], []
    for p in paths:
        text = Path(p).read_text(encoding="utf-8")
        blocks, stats = parse(text)
        src_head = len(re.findall(r"^\s*#{1,6}\s", text, re.M))
        src_tables = len(re.findall(r"^\|.+\|\s*$", text, re.M))
        src_bullets = len(re.findall(r"^\s*(?:[-*+]|\d+[.)])\s+", text, re.M))
        src_fences = text.count("```") // 2
        out.append({"source": Path(p).name, "path": str(p), "blocks": blocks})
        report.append({
            "file": Path(p).name,
            "lines": len(text.split("\n")),
            "chars": len(text),
            "src_headings": src_head, "out_headings": stats["heading"],
            "src_table_lines": src_tables, "out_tables": stats["table"],
            "out_table_rows": stats["tablerow"],
            "src_bullets": src_bullets, "out_bullets": stats["bullet"],
            "src_code_fences": src_fences, "out_code": stats["code"],
            "out_paras": stats["para"], "out_quotes": stats["quote"],
        })
    return out, report


REPO = Path(__file__).resolve().parent.parent
SOURCES = sorted((REPO / "sources").glob("*.md"))   # numeric prefixes fix the order

if __name__ == "__main__":
    docs, report = build(SOURCES)
    dest = REPO / "_build"
    dest.mkdir(parents=True, exist_ok=True)
    (dest / "content.json").write_text(json.dumps(docs, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(report, indent=1))
    tot = {k: sum(r[k] for r in report) for k in report[0] if k not in ("file",)}
    print("\nTOTALS", json.dumps(tot))
    missing = [(r["file"], r["src_headings"], r["out_headings"], r["src_bullets"], r["out_bullets"])
               for r in report if r["src_headings"] != r["out_headings"] or r["src_bullets"] != r["out_bullets"]]
    print("MISMATCH", missing if missing else "none")
