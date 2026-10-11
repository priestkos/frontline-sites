#!/usr/bin/env python3
"""Builds the unabridged archive site: 'The Woodblock Codex'.

Paper + iron-gall ink + one vermilion seal. Everything inline: no CDN, no
external image, no font fetch, no host gate. Opens by double-click, offline.
"""
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from md2blocks import build, SOURCES  # noqa: E402

OUT = Path(__file__).resolve().parent.parent / "woodblock-codex"
OUT.mkdir(parents=True, exist_ok=True)

DOCS, REPORT = build(SOURCES)
BLOCK_BUDGET = sum(len(d["blocks"]) for d in DOCS)

# ------------------------------------------------------------------ rendering
def render_blocks(blocks, doc_idx):
    h = []
    for b in blocks:
        t = b["type"]
        if t == "heading":
            lv = min(b["level"], 4)
            ident = f"d{doc_idx}-{b['id']}"
            h.append(f'<h{lv} id="{ident}" class="blk-h lv{lv}">{b["html"]}</h{lv}>')
        elif t == "para":
            h.append(f'<p class="blk-p">{b["html"]}</p>')
        elif t == "table":
            head = "".join(f"<th>{c}</th>" for c in b["head"])
            rows = "".join(
                "<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in b["rows"])
            h.append(f'<div class="tbl-wrap"><table class="blk-tbl"><thead><tr>{head}</tr></thead>'
                     f"<tbody>{rows}</tbody></table></div>")
        elif t == "list":
            tag = b["kind"]
            items = "".join(f"<li>{it['html']}</li>" for it in b["items"])
            h.append(f'<{tag} class="blk-list{" nested" if b["depth"] else ""}">{items}</{tag}>')
        elif t == "code":
            h.append(f'<div class="code-wrap"><button class="copy" type="button" data-copy>COPY</button>'
                     f'<pre class="blk-code"><code>{b["text"].replace("&","&amp;").replace("<","&lt;")}</code></pre></div>')
        elif t == "quote":
            h.append(f'<blockquote class="blk-q">{b["html"]}</blockquote>')
        elif t == "rule":
            h.append('<hr class="blk-rule">')
        elif t == "anchor":
            h.append(f'<span id="d{doc_idx}-{b["id"]}" class="anchor"></span>')
    return "\n".join(h)


# Titles keyed by POSITION, not by basename: two of the sources are both named
# SKILL.md, and a basename key silently gave document VII document V's heading.
DOC_TITLES = [
    ("The Complete Field Guide",
     "Eighteen parts. Mechanics, all five maps, the five levers, doctrine, the fourteen named plays, command, and the quick reference."),
    ("Jobs, Roles and How They Interact",
     "Twenty-one jobs, five roles, all fifteen role actions, the kill chain, counter-pairs, and the map-affinity matrix."),
    ("The Callout Macro Pack",
     "Twenty-seven bilingual callouts, the sound convention, hotbar layout, auto-translate appendix and the Japanese glossary."),
    ("The Call Sheet",
     "The one-page caller reference: calls, rules of engagement, phase script, timings and the live decision table."),
    ("Frontline, Condensed",
     "The briefing form of the doctrine: mechanics, per-map playbook, the named plays and the standing orders."),
    ("Military Doctrine",
     "The primary sources: the nine principles, Lanchester's laws, Clausewitz, Liddell Hart, Boyd, Jomini and Sun Tzu."),
    ("Macro Authoring",
     "How FFXIV macros actually work: the hard limits, the eight silent failure modes, the command reference and the bilingual trap."),
]
ROMAN = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII"]
assert len(DOCS) == len(DOC_TITLES), f"{len(DOCS)} sources but {len(DOC_TITLES)} titles"

toc, body = [], []
for idx, doc in enumerate(DOCS):
    title, blurb = DOC_TITLES[idx]
    num = ROMAN[idx]
    body.append(
        f'<section class="doc" id="doc-{idx}" data-doc="{idx}">'
        f'<header class="doc-head"><span class="doc-numeral" aria-hidden="true">{num}</span>'
        f'<p class="doc-kicker">Document {idx + 1} of {len(DOCS)}</p>'
        f'<h2 class="doc-title">{title}</h2><p class="doc-blurb">{blurb}</p></header>'
        f'<div class="doc-body">{render_blocks(doc["blocks"], idx)}</div></section>')
    subs = []
    for b in doc["blocks"]:
        if b["type"] == "heading" and b["level"] in (1, 2, 3):
            subs.append((min(b["level"], 3), b["text"][:76], f'd{idx}-{b["id"]}'))
    toc.append({"idx": idx, "num": num, "title": title, "blurb": blurb, "subs": subs})

BLOCKS_JSON = json.dumps([{"num": t["num"], "title": t["title"], "subs": t["subs"]} for t in toc],
                         ensure_ascii=False)

# charts --------------------------------------------------------------------
THRESH = [("Onsal Hakair", 1400, "Danshig Naadam"), ("Worqor Chirteh", 1400, "Triumph"),
          ("Fields of Glory", 1600, "Shatter"), ("Seal Rock", 2000, "Seize"),
          ("Borderland Ruins", 2400, "Secure")]
NODE_TICK = [2, 4, 6, 10, 12, 14, 18, 20, 22]
OVOO = [("B", 50, 5), ("A", 100, 10), ("S", 200, 20)]
OVOO_DECAY = [(30, 200), (20, 120), (15, 100), (10, 60), (6, 40)]
BH_KO = [4, 6, 8, 12, 16, 20]
BH_LABEL = ["none", "I", "II", "III", "IV", "V"]
AFFINITY = [
    ("Paladin", [3, 3, 4, 4, 3]), ("Warrior", [4, 3, 4, 4, 4]), ("Dark Knight", [4, 4, 3, 3, 4]),
    ("Gunbreaker", [4, 3, 3, 3, 3]), ("White Mage", [3, 4, 4, 4, 3]), ("Scholar", [1, 1, 1, 1, 1]),
    ("Astrologian", [3, 4, 4, 4, 3]), ("Sage", [3, 2, 3, 3, 3]), ("Monk", [3, 3, 2, 3, 3]),
    ("Dragoon", [4, 3, 4, 4, 4]), ("Ninja", [3, 3, 3, 3, 4]), ("Samurai", [4, 4, 3, 3, 3]),
    ("Reaper", [4, 4, 4, 3, 4]), ("Viper", [4, 3, 4, 3, 4]), ("Bard", [2, 1, 3, 3, 2]),
    ("Machinist", [2, 2, 3, 3, 2]), ("Dancer", [4, 4, 4, 4, 4]), ("Black Mage", [3, 3, 4, 4, 4]),
    ("Summoner", [3, 4, 3, 3, 3]), ("Red Mage", [3, 2, 4, 4, 3]), ("Pictomancer", [3, 3, 3, 4, 3]),
]
MAPS = ["Secure", "Seize", "Shatter", "Naadam", "Triumph"]
ROLE_ACTIONS = [
    ("Tank", "Rampage, Rampart, Full Swing", "Rampage: +25% damage taken on targets, 45s"),
    ("Melee", "Bloodbath, Swift, Smite", "Smite: ignores Guard, resets on every KO, 15s"),
    ("Physical ranged", "Dervish, Bravery, Eagle Eye", "Bravery: +25% dealt and -25% taken, 30s"),
    ("Magical ranged", "Comet, Phantom Dart, Rust", "Phantom Dart: +25% damage taken, 15s"),
    ("Healer", "Haelan, Stoneskin II, Diabrosis", "Diabrosis: -33% healing received, 45s"),
]


def bar_chart():
    mx = 2400
    rows = []
    for label, val, sub in THRESH:
        w = val / mx * 100
        rows.append(
            f'<div class="bar-row"><span class="bar-label">{label}<em>{sub}</em></span>'
            f'<span class="bar-track"><span class="bar-fill" style="--w:{w:.1f}%" data-val="{val}"></span></span>'
            f'<span class="bar-val mono" data-count="{val}">{val}</span></div>')
    return "".join(rows)


def line_chart(points, w=560, h=200, pad=34, labels=None, fill=True, accent_pts=None):
    mx = max(v for _, v in points)
    n = len(points)
    def xy(i, v):
        x = pad + i * (w - 2 * pad) / (n - 1)
        y = h - pad - (v / mx) * (h - 2 * pad)
        return x, y
    d = " ".join(("M" if i == 0 else "L") + f"{xy(i, v)[0]:.1f},{xy(i, v)[1]:.1f}"
                 for i, (_, v) in enumerate(points))
    area = d + f" L{xy(n - 1, 0)[0]:.1f},{h - pad} L{xy(0, 0)[0]:.1f},{h - pad} Z"
    grid = "".join(f'<line x1="{pad}" y1="{h - pad - g * (h - 2 * pad) / 4:.1f}" '
                   f'x2="{w - pad}" y2="{h - pad - g * (h - 2 * pad) / 4:.1f}" class="grid"/>'
                   for g in range(5))
    dots = "".join(f'<circle cx="{xy(i, v)[0]:.1f}" cy="{xy(i, v)[1]:.1f}" r="3.4" class="dot">'
                   f'<title>{labels[i] if labels else i}: {v}</title></circle>'
                   for i, (_, v) in enumerate(points))
    lab = ""
    if labels:
        step = max(1, n // 6)
        lab = "".join(f'<text x="{xy(i, 0)[0]:.1f}" y="{h - pad + 16}" class="axis">{labels[i]}</text>'
                      for i in range(0, n, step))
    fillp = f'<path d="{area}" class="area"/>' if fill else ""
    return (f'<svg class="chart-svg" viewBox="0 0 {w} {h}" role="img" aria-label="chart">'
            f'{grid}{fillp}<path d="{d}" class="line"/>'
            f'<path d="{d}" class="line-draw"/>{dots}{lab}</svg>')


def heatmap():
    cells = []
    for r, (name, vals) in enumerate(AFFINITY):
        cells.append(f'<div class="hm-name">{name}</div>')
        for c, v in enumerate(vals):
            cells.append(
                f'<div class="hm-cell lv{v}" title="{name} on {MAPS[c]}: {["poor","situational","good","excellent"][v-1]}">'
                f'<span class="sr">{name} on {MAPS[c]}</span></div>')
    head = "".join(f'<div class="hm-head">{m}</div>' for m in MAPS)
    return (f'<div class="hm" style="--cols:{len(MAPS)}"><div class="hm-corner">Job</div>{head}'
            + "".join(cells) + "</div>")


CHART_TABS = [
    ("thresholds", "Win thresholds", bar_chart(),
     "Every campaign is a threshold, never a kill count. The number is the objective."),
    ("nodes", "Secure node income", line_chart([(i + 1, v) for i, v in enumerate(NODE_TICK)],
                                                labels=[str(i + 1) for i in range(9)]),
     "Tactical rating per 3 seconds by key locations held. Four nodes is the breakpoint."),
    ("ovoo", "Ovoo payout and decay",
     line_chart(OVOO_DECAY, w=540, h=190,
                labels=[f"{s}s" for s, _ in OVOO_DECAY]),
     "An ovoo pays for 30 seconds. End the match early and you keep only the ticks that landed."),
    ("high", "Battle High and the kill",
     line_chart([(i, v) for i, v in enumerate(BH_KO)], w=540, h=190, labels=BH_LABEL),
     "KO rating scales with the victim's tier: 4 at none, 20 at Battle High V."),
    ("lanchester", "Lanchester: square against linear",
     line_chart([(n, n * n) for n in range(1, 9)], w=540, h=190,
                labels=[str(n) for n in range(1, 9)]),
     "Aimed fire scales combat power with the square of numbers. Double the side, quadruple the power."),
    ("affinity", "Job by map affinity", heatmap(),
     "Twenty-one jobs against the five maps. The saturated cells are where a job is worth playing."),
]

ROLE_ROWS = "".join(
    f'<div class="ra-row"><span class="ra-role">{r}</span><span class="ra-set">{s}</span>'
    f'<span class="ra-note">{n}</span></div>' for r, s, n in ROLE_ACTIONS)

CSS = r"""
<style>
:root{
  --paper:#f2f1ec; --panel:#fffefb; --ink:#16181a; --muted:#5f6368; --faint:#8b8f90;
  --rule:#d6d3c9; --rule-2:#bdb9ad; --seal:#d5432a; --seal-d:#a8321f; --wash:#e7e5dc;
  --hero-a:#fbfaf6; --hero-b:#efece2; --ink-2:#333; --on-ink:#fff; --ink-rgb:22,24,26;
  --th-bg:#eceae1; --th-ink:#43474a; --row-hover:#faf9f4; --code-bg:#16181a; --code-ink:#eceae1;
  --copy-bg:#2a2d31; --copy-ink:#cfcabc; --copy-bd:#3c4045; --hm1:#e4e2d9; --hm2:#c9c6b8; --hm3:#8d8a7c;
  --serif: ui-serif, "Iowan Old Style", "Palatino Linotype", Palatino, Georgia, serif;
  --sans: ui-sans-serif, system-ui, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  --mono: ui-monospace, "Cascadia Mono", "SF Mono", Menlo, Consolas, monospace;
  --r:2px; --maxw:1440px;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--paper);color:var(--ink);font-family:var(--sans);
  font-size:17px;line-height:1.62;-webkit-font-smoothing:antialiased}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
::selection{background:var(--seal);color:var(--on-ink)}
a,button{font-family:inherit}
.mono{font-family:var(--mono);font-variant-numeric:tabular-nums}

/* ---------- progress + shell ---------- */
.progress{position:fixed;top:0;left:0;height:3px;background:var(--seal);width:0;z-index:60}
.shell{max-width:var(--maxw);margin:0 auto;padding:0 28px}
.layout{display:grid;grid-template-columns:288px minmax(0,1fr);gap:56px;align-items:start}
@media(max-width:1040px){.layout{grid-template-columns:1fr;gap:24px}}

/* ---------- hero ---------- */
.hero{position:relative;overflow:hidden;border-bottom:1px solid var(--rule);
  background:linear-gradient(180deg,var(--hero-a),var(--hero-b))}
.hero-ink{position:absolute;inset:0;width:100%;height:100%;opacity:.5}
.seigaiha{position:absolute;left:0;right:0;bottom:0;height:120px;opacity:.5;
  background-image:radial-gradient(circle at 50% 100%,transparent 34%,var(--rule-2) 35%,transparent 37%),
  radial-gradient(circle at 50% 100%,transparent 34%,var(--rule-2) 35%,transparent 37%);
  background-size:56px 28px,56px 28px;background-position:0 0,28px 0}
.hero-inner{position:relative;z-index:2;padding:104px 0 84px;max-width:900px}
.seal{display:inline-flex;align-items:center;gap:12px;border:1px solid var(--seal);
  color:var(--seal-d);padding:7px 13px;border-radius:var(--r);font-family:var(--mono);
  font-size:11.5px;letter-spacing:.16em;text-transform:uppercase}
.seal b{display:block;width:7px;height:7px;background:var(--seal);border-radius:50%}
h1.title{font-family:var(--serif);font-weight:600;font-size:clamp(48px,8.4vw,116px);
  line-height:.94;letter-spacing:-.02em;margin:26px 0 0}
h1.title em{font-style:normal;color:var(--seal-d)}
.lede{margin:26px 0 0;max-width:62ch;font-size:19px;color:var(--ink-2)}
.hero-meta{display:flex;flex-wrap:wrap;gap:34px;margin-top:44px;padding-top:22px;
  border-top:1px solid var(--rule-2)}
.hero-meta div{font-family:var(--mono);font-size:11.5px;letter-spacing:.1em;
  text-transform:uppercase;color:var(--muted)}
.hero-meta b{display:block;font-family:var(--serif);font-size:30px;letter-spacing:0;
  text-transform:none;color:var(--ink);margin-top:6px}
.cta-row{display:flex;flex-wrap:wrap;gap:14px;margin-top:40px}
.cta-open{display:inline-flex;align-items:center;gap:12px;background:var(--ink);color:var(--on-ink);
  border:0;padding:15px 22px;font-size:14px;letter-spacing:.02em;cursor:pointer;
  border-radius:var(--r);text-decoration:none;transition:transform .18s,background .18s}
.cta-open:hover{background:var(--seal-d);transform:translateY(-1px)}
.cta-open:active{transform:translateY(0) scale(.99)}
.cta-open i{width:26px;height:1px;background:var(--on-ink);display:block;position:relative}
.cta-open i::after{content:"";position:absolute;right:0;top:-3px;width:7px;height:7px;
  border-top:1px solid var(--on-ink);border-right:1px solid var(--on-ink);transform:rotate(45deg)}
.cta-quiet{display:inline-flex;align-items:center;gap:10px;background:none;border:0;
  border-bottom:1px solid var(--rule-2);color:var(--ink);padding:15px 2px;cursor:pointer;
  font-size:14px;text-decoration:none;transition:border-color .18s,color .18s}
.cta-quiet:hover{border-color:var(--seal);color:var(--seal-d)}

/* ---------- rail ---------- */
.rail{position:sticky;top:22px;max-height:calc(100vh - 44px);overflow:auto;
  border-top:2px solid var(--ink);padding-top:14px}
.rail-h{font-family:var(--mono);font-size:11px;letter-spacing:.18em;text-transform:uppercase;
  color:var(--muted);margin:0 0 12px}
.filter{width:100%;border:1px solid var(--rule-2);background:var(--panel);padding:9px 11px;
  font-family:var(--mono);font-size:12.5px;border-radius:var(--r);margin-bottom:14px}
.filter:focus{outline:2px solid var(--seal);outline-offset:1px}
.rail-doc{border-bottom:1px solid var(--rule);padding:9px 0}
.rail-doc>a{display:grid;grid-template-columns:26px 1fr;gap:8px;text-decoration:none;color:var(--ink)}
.rail-doc>a:hover .rail-t{color:var(--seal-d)}
.rail-n{font-family:var(--mono);font-size:11px;color:var(--seal-d);padding-top:3px}
.rail-t{font-size:14.5px;font-weight:600;line-height:1.35}
.rail-subs{list-style:none;margin:6px 0 4px;padding:0}
.rail-subs a{display:block;font-size:12.8px;color:var(--muted);text-decoration:none;
  padding:3.5px 0 3.5px 34px;border-left:1px solid var(--rule)}
.rail-subs a:hover{color:var(--seal-d);border-left-color:var(--seal)}
.rail-subs li.hide,.rail-doc.hide{display:none}
@media(max-width:1040px){.rail{position:static;max-height:none}}

/* ---------- sections ---------- */
main{padding:72px 0 120px;min-width:0}
.sec{margin:0 0 92px;scroll-margin-top:20px}
.sec-head{display:grid;grid-template-columns:auto 1fr;gap:20px;align-items:baseline;
  border-top:2px solid var(--ink);padding-top:16px;margin-bottom:30px}
.sec-num{font-family:var(--serif);font-size:44px;line-height:1;color:var(--seal-d)}
.sec-t{font-family:var(--serif);font-size:clamp(26px,3.4vw,40px);margin:0;font-weight:600;
  letter-spacing:-.01em}
.sec-sub{margin:8px 0 0;color:var(--muted);font-size:15.5px;max-width:70ch}

/* ---------- dashboards ---------- */
.dash{display:grid;grid-template-columns:220px minmax(0,1fr);gap:26px;align-items:start}
@media(max-width:860px){.dash{grid-template-columns:1fr}}
.tabs{display:flex;flex-direction:column;border-top:1px solid var(--rule)}
@media(max-width:860px){.tabs{flex-direction:row;flex-wrap:wrap}}
.tab{text-align:left;background:none;border:0;border-bottom:1px solid var(--rule);
  padding:11px 4px;font-size:14px;color:var(--muted);cursor:pointer;transition:color .15s,padding .15s}
@media(max-width:860px){.tab{border:1px solid var(--rule);padding:7px 10px;margin:0 6px 6px 0}}
.tab:hover{color:var(--ink)}
.tab[aria-selected="true"]{color:var(--seal-d);border-bottom-color:var(--seal);
  padding-left:8px;font-weight:600}
.panel{border:1px solid var(--rule);background:var(--panel);padding:26px;border-radius:var(--r)}
.panel[hidden]{display:none}
.panel h3{margin:0 0 6px;font-family:var(--serif);font-size:23px;font-weight:600}
.panel p{margin:0 0 18px;color:var(--muted);font-size:14.5px;max-width:74ch}
.chart-svg{width:100%;height:auto;display:block;overflow:visible}
.grid{stroke:var(--rule);stroke-width:1}
.area{fill:var(--wash);opacity:.85}
.line{fill:none;stroke:var(--ink);stroke-width:2.1;stroke-linejoin:round}
.line-draw{fill:none;stroke:var(--seal);stroke-width:2.1;stroke-linejoin:round;
  stroke-dasharray:1400;stroke-dashoffset:1400}
.in .line-draw{animation:draw 1.9s cubic-bezier(.5,0,.2,1) forwards}
@keyframes draw{to{stroke-dashoffset:0}}
.dot{fill:var(--seal)}
.axis{font-family:var(--mono);font-size:10.5px;fill:var(--faint);text-anchor:middle}
.bar-row{display:grid;grid-template-columns:190px 1fr 68px;gap:14px;align-items:center;
  padding:9px 0;border-bottom:1px solid var(--rule)}
.bar-label{font-size:14.5px}
.bar-label em{display:block;font-style:normal;font-family:var(--mono);font-size:11px;
  color:var(--faint);letter-spacing:.06em}
.bar-track{height:14px;background:var(--wash);position:relative;border-radius:1px;overflow:hidden}
.bar-fill{position:absolute;inset:0 auto 0 0;width:0;background:var(--ink);border-right:2px solid var(--seal)}
.in .bar-fill{animation:grow 1.5s cubic-bezier(.4,0,.2,1) forwards;width:var(--w)}
@keyframes grow{from{width:0}to{width:var(--w)}}
.bar-val{text-align:right;font-size:14px;color:var(--seal-d);font-weight:600}
.hm{display:grid;grid-template-columns:120px repeat(var(--cols),minmax(0,1fr));gap:3px}
.hm-corner,.hm-head{font-family:var(--mono);font-size:10.5px;letter-spacing:.08em;
  text-transform:uppercase;color:var(--faint);padding:4px 0;text-align:center}
.hm-corner{text-align:left}
.hm-name{font-size:12.6px;color:var(--ink);padding:4px 6px 4px 0;border-right:1px solid var(--rule)}
.hm-cell{aspect-ratio:1.9/1;border-radius:1px;background:var(--wash)}
.hm-cell.lv1{background:var(--hm1)}.hm-cell.lv2{background:var(--hm2)}
.hm-cell.lv3{background:var(--hm3)}.hm-cell.lv4{background:var(--seal)}
.hm-cell:hover{outline:2px solid var(--ink);outline-offset:-2px}
@media(max-width:860px){.hm{grid-template-columns:86px repeat(var(--cols),minmax(0,1fr))}}
.ra-row{display:grid;grid-template-columns:150px 1fr 1fr;gap:16px;padding:11px 0;
  border-bottom:1px solid var(--rule);font-size:14px}
@media(max-width:760px){.ra-row{grid-template-columns:1fr}}
.ra-role{font-weight:600}
.ra-set{font-family:var(--mono);font-size:12.5px;color:var(--muted)}
.ra-note{color:var(--seal-d);font-size:13px}

/* ---------- archive ---------- */
.doc{border-top:1px solid var(--rule);padding-top:44px;margin-bottom:86px;scroll-margin-top:14px}
.doc-head{position:relative;margin-bottom:34px}
.doc-numeral{position:absolute;right:0;top:-22px;font-family:var(--serif);font-size:150px;
  line-height:.8;color:var(--wash);z-index:0;user-select:none}
.doc-kicker{font-family:var(--mono);font-size:11px;letter-spacing:.2em;text-transform:uppercase;
  color:var(--seal-d);margin:0 0 10px;position:relative;z-index:1}
.doc-title{font-family:var(--serif);font-size:clamp(30px,4.4vw,52px);margin:0;font-weight:600;
  letter-spacing:-.015em;position:relative;z-index:1;max-width:22ch}
.doc-blurb{position:relative;z-index:1;margin:14px 0 0;color:var(--muted);max-width:74ch;font-size:16px}
.doc-body{position:relative;z-index:1}
.blk-h{font-family:var(--serif);letter-spacing:-.01em;scroll-margin-top:16px}
.lv1{font-size:34px;margin:52px 0 14px;border-bottom:1px solid var(--rule-2);padding-bottom:8px}
.lv2{font-size:25px;margin:40px 0 12px}
.lv3{font-size:19px;margin:30px 0 8px;font-family:var(--sans);font-weight:700;letter-spacing:0}
.lv4{font-size:15.5px;margin:22px 0 6px;font-family:var(--mono);text-transform:uppercase;
  letter-spacing:.1em;color:var(--seal-d)}
.blk-p{margin:0 0 15px;max-width:78ch}
.blk-list{margin:0 0 16px;padding-left:22px;max-width:78ch}
.blk-list li{margin:0 0 6px}
.blk-list.nested{margin-top:-8px;color:var(--ink-2)}
.blk-q{margin:22px 0;padding:14px 20px;border-left:3px solid var(--seal);background:var(--panel);
  font-family:var(--serif);font-size:18px;max-width:74ch}
.blk-rule{border:0;border-top:1px solid var(--rule-2);margin:32px 0}
.tbl-wrap{overflow-x:auto;margin:0 0 22px;border:1px solid var(--rule-2);background:var(--panel)}
table.blk-tbl{border-collapse:collapse;width:100%;font-size:14px;min-width:520px}
.blk-tbl th{background:var(--th-bg);text-align:left;font-family:var(--mono);font-size:11px;
  letter-spacing:.08em;text-transform:uppercase;color:var(--th-ink);padding:10px 12px;
  border-bottom:1px solid var(--rule-2);white-space:nowrap}
.blk-tbl td{padding:9px 12px;border-bottom:1px solid var(--rule);vertical-align:top}
.blk-tbl tr:hover td{background:var(--row-hover)}
.code-wrap{position:relative;margin:0 0 22px}
.blk-code{background:var(--code-bg);color:var(--code-ink);padding:20px 18px;overflow-x:auto;font-family:var(--mono);
  font-size:13px;line-height:1.6;border-radius:var(--r);margin:0}
.copy{position:absolute;top:8px;right:8px;background:var(--copy-bg);color:var(--copy-ink);border:1px solid var(--copy-bd);
  font-family:var(--mono);font-size:10.5px;letter-spacing:.1em;padding:5px 9px;cursor:pointer;
  border-radius:var(--r)}
.copy:hover{background:var(--seal);border-color:var(--seal);color:#fff}
.cite{color:var(--seal-d);border-bottom:1px dotted var(--seal)}
.cite-url{font-family:var(--mono);font-size:11.5px;color:var(--faint);margin-left:6px;word-break:break-all}
.anchor{display:block;height:0}

/* ---------- reveal ---------- */
.rise{opacity:1;transform:none}
html.motion .rise{opacity:0;transform:translateY(16px)}
html.motion .rise.in{opacity:1;transform:none;transition:opacity .6s ease,transform .6s cubic-bezier(.2,.7,.2,1)}
footer{border-top:1px solid var(--rule-2);padding:40px 0 70px;color:var(--muted);font-size:13px}
.foot-row{display:flex;flex-wrap:wrap;gap:26px;justify-content:space-between}
@media(prefers-reduced-motion:reduce){
  html{scroll-behavior:auto}
  html.motion .rise{opacity:1;transform:none}
  .in .bar-fill{animation:none;width:var(--w)}
  .in .line-draw{animation:none;stroke-dashoffset:0}
}
/* ---------- theme: dark (Ink Night) ---------- */
:root[data-theme="dark"]{
  --paper:#121315; --panel:#1b1d20; --ink:#ecebe6; --muted:#a4a7a8; --faint:#7d8183;
  --rule:#2c2f33; --rule-2:#44484d; --seal:#e5533a; --seal-d:#f0826d; --wash:#25282c;
  --hero-a:#18191c; --hero-b:#0d0e10; --ink-2:#d6d5cf; --on-ink:#121315; --ink-rgb:236,235,230;
  --th-bg:#23262a; --th-ink:#b9bcbd; --row-hover:#202326; --code-bg:#08090a; --code-ink:#e6e4dc;
  --copy-bg:#24272b; --copy-ink:#cfcabc; --copy-bd:#3c4045; --hm1:#2a2d31; --hm2:#3d4147; --hm3:#6b6f74;
  color-scheme:dark;
}
:root[data-theme="dark"] ::selection{color:#fff}
body{transition:background-color .35s ease,color .35s ease}
.seal-svg .k{stroke:var(--ink)}
.seal-svg .s{stroke:var(--seal)}
.seal-svg .d{fill:var(--seal)}
.theme-toggle{position:fixed;top:14px;right:16px;z-index:70;display:inline-flex;align-items:center;gap:10px;
  background:var(--panel);color:var(--ink);border:1px solid var(--rule-2);border-radius:var(--r);
  padding:8px 12px;font-family:var(--mono);font-size:11px;letter-spacing:.14em;text-transform:uppercase;cursor:pointer;
  transition:border-color .2s,color .2s}
.theme-toggle:hover{border-color:var(--seal);color:var(--seal-d)}
.theme-toggle:focus-visible{outline:2px solid var(--seal);outline-offset:2px}
.theme-toggle .sw{position:relative;width:26px;height:14px;border:1px solid currentColor;border-radius:8px;display:inline-block}
.theme-toggle .sw::after{content:"";position:absolute;top:2px;left:2px;width:8px;height:8px;border-radius:50%;
  background:currentColor;transition:transform .25s ease}
:root[data-theme="dark"] .theme-toggle .sw::after{transform:translateX(12px)}
</style>
"""

JS = r"""
<script>
(function(){
  var html=document.documentElement;
  var reduce=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if(!reduce){html.classList.add('motion');}

  /* progress bar */
  var bar=document.querySelector('.progress');
  function onScroll(){
    var h=document.documentElement.scrollHeight-window.innerHeight;
    bar.style.width=(h>0?(window.scrollY/h)*100:0)+'%';
  }
  addEventListener('scroll',onScroll,{passive:true});onScroll();

  /* reveals: never leave content hidden */
  var items=[].slice.call(document.querySelectorAll('.rise, .sec, .panel'));
  function show(el){el.classList.add('in');}
  if(!reduce&&'IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){
      es.forEach(function(e){if(e.isIntersecting){show(e.target);io.unobserve(e.target);}});
    },{rootMargin:'0px 0px -8% 0px'});
    items.forEach(function(el){io.observe(el);});
    setTimeout(function(){items.forEach(show);},2500);      /* hard safety net */
    addEventListener('load',function(){items.forEach(function(el){
      var r=el.getBoundingClientRect(); if(r.top<innerHeight*1.2){show(el);}
    });});
  } else { items.forEach(show); }

  /* counters */
  function count(el){
    var to=parseInt(el.getAttribute('data-count'),10),i=0;
    if(reduce||!to){el.textContent=to.toLocaleString();return;}
    var step=Math.max(1,Math.round(to/38));
    var id=setInterval(function(){i+=step;if(i>=to){i=to;clearInterval(id);}
      el.textContent=i.toLocaleString();},22);
  }
  var co=new IntersectionObserver(function(es){es.forEach(function(e){
    if(e.isIntersecting){count(e.target);co.unobserve(e.target);}});},{threshold:.3});
  [].slice.call(document.querySelectorAll('[data-count]')).forEach(function(el){
    if(reduce){el.textContent=parseInt(el.getAttribute('data-count'),10).toLocaleString();return;}
    co.observe(el);});

  /* dashboards */
  [].slice.call(document.querySelectorAll('[data-tabs]')).forEach(function(group){
    var tabs=[].slice.call(group.querySelectorAll('[role=tab]'));
    tabs.forEach(function(t){
      t.addEventListener('click',function(){
        tabs.forEach(function(x){x.setAttribute('aria-selected',x===t?'true':'false');
          var p=document.getElementById(x.getAttribute('aria-controls'));
          if(p){p.hidden=(x!==t);} });
        var active=document.getElementById(t.getAttribute('aria-controls'));
        if(active){active.classList.add('in');}
      });
    });
  });

  /* copy buttons */
  document.addEventListener('click',function(e){
    var b=e.target.closest&&e.target.closest('[data-copy]'); if(!b)return;
    var pre=b.parentNode.querySelector('code'); if(!pre)return;
    var txt=pre.innerText;
    var done=function(){b.textContent='COPIED';setTimeout(function(){b.textContent='COPY';},1400);};
    if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(txt).then(done,function(){done();});}
    else{var ta=document.createElement('textarea');ta.value=txt;document.body.appendChild(ta);
      ta.select();try{document.execCommand('copy');}catch(err){}document.body.removeChild(ta);done();}
  });

  /* rail filter */
  var f=document.getElementById('railFilter');
  if(f){
    f.addEventListener('input',function(){
      var q=f.value.trim().toLowerCase();
      [].slice.call(document.querySelectorAll('.rail-doc')).forEach(function(d){
        var hit=d.textContent.toLowerCase().indexOf(q)>-1;
        d.classList.toggle('hide',q&&!hit);
        [].slice.call(d.querySelectorAll('.rail-subs li')).forEach(function(li){
          li.classList.toggle('hide',q&&li.textContent.toLowerCase().indexOf(q)<0);
        });
      });
    });
  }

  /* theme switcher */
  var tbtn=document.getElementById('themeToggle'),tlab=document.getElementById('themeLabel');
  function applyTheme(dark){
    if(dark){html.setAttribute('data-theme','dark');}else{html.removeAttribute('data-theme');}
    tbtn.setAttribute('aria-pressed',dark?'true':'false');
    tbtn.setAttribute('aria-label',dark?'Switch to light theme':'Switch to dark theme');
    tlab.textContent=dark?'Light theme':'Dark theme';
  }
  applyTheme(html.getAttribute('data-theme')==='dark');
  tbtn.addEventListener('click',function(){
    var dark=html.getAttribute('data-theme')!=='dark';
    applyTheme(dark);
    try{localStorage.setItem('codex-theme',dark?'dark':'light');}catch(e){}
  });

  /* ink wash canvas */
  var cv=document.getElementById('inkCanvas');
  if(cv&&!reduce){
    var ctx=cv.getContext('2d'),w,h,blobs=[];
    function size(){w=cv.width=cv.offsetWidth;h=cv.height=cv.offsetHeight;}
    size();addEventListener('resize',size);
    for(var i=0;i<16;i++){blobs.push({x:Math.random(),y:Math.random(),
      r:40+Math.random()*120,vx:(Math.random()-.5)*.0006,vy:(Math.random()-.5)*.0004});}
    (function loop(){
      ctx.clearRect(0,0,w,h);
      blobs.forEach(function(b){
        b.x+=b.vx;b.y+=b.vy;
        if(b.x<-.2||b.x>1.2)b.vx*=-1; if(b.y<-.2||b.y>1.2)b.vy*=-1;
        var g=ctx.createRadialGradient(b.x*w,b.y*h,0,b.x*w,b.y*h,b.r);
        var rgb=getComputedStyle(html).getPropertyValue('--ink-rgb').trim()||'22,24,26';
        g.addColorStop(0,'rgba('+rgb+',0.045)');g.addColorStop(1,'rgba('+rgb+',0)');
        ctx.fillStyle=g;ctx.beginPath();ctx.arc(b.x*w,b.y*h,b.r,0,6.284);ctx.fill();
      });
      requestAnimationFrame(loop);
    })();
  }

  /* stroke-draw the seal on load */
  var paths=[].slice.call(document.querySelectorAll('.seal-svg path, .seal-svg circle'));
  if(paths.length&&!reduce){
    paths.forEach(function(p,i){
      var len=0; try{len=p.getTotalLength();}catch(e){len=0;}
      if(!len)return;
      p.style.strokeDasharray=len;p.style.strokeDashoffset=len;
      p.style.transition='stroke-dashoffset 1.5s cubic-bezier(.4,0,.2,1) '+(i*0.12)+'s';
      requestAnimationFrame(function(){p.style.strokeDashoffset=0;});
    });
  }
})();
</script>
"""

SEAL_SVG = """
<svg class="seal-svg" width="132" height="132" viewBox="0 0 132 132" aria-hidden="true">
  <circle cx="66" cy="66" r="60" fill="none" class="k" stroke="#16181a" stroke-width="1.4"/>
  <circle cx="66" cy="66" r="50" fill="none" class="s" stroke="#d5432a" stroke-width="1"/>
  <path d="M40 84c10-6 16-18 18-32 3 14 9 26 19 32" fill="none" class="k" stroke="#16181a" stroke-width="2.1"/>
  <path d="M36 62c14 4 26 4 40-2" fill="none" class="k" stroke="#16181a" stroke-width="1.6"/>
  <path d="M58 52l8-14 8 14" fill="none" class="s" stroke="#d5432a" stroke-width="1.8"/>
  <path d="M46 96h40" fill="none" class="k" stroke="#16181a" stroke-width="1.4"/>
  <circle cx="66" cy="30" r="3" class="d" fill="#d5432a"/>
</svg>"""

TOC_HTML = "".join(
    f'<div class="rail-doc" data-doc="{t["idx"]}"><a href="#doc-{t["idx"]}">'
    f'<span class="rail-n">{t["num"]}</span><span class="rail-t">{t["title"]}</span></a>'
    f'<ul class="rail-subs">' +
    "".join(f'<li><a href="#{sid}">{txt}</a></li>' for _, txt, sid in t["subs"]) +
    "</ul></div>" for t in toc)

TABS_HTML = "".join(
    f'<button class="tab" role="tab" aria-selected="{"true" if i == 0 else "false"}" '
    f'aria-controls="panel-{cid}">{label}</button>' for i, (cid, label, _, _) in enumerate(CHART_TABS))
PANELS_HTML = "".join(
    f'<div class="panel" id="panel-{cid}" role="tabpanel"{" hidden" if i else ""}>'
    f'<h3>{label}</h3><p>{desc}</p>{svg}</div>' for i, (cid, label, svg, desc) in enumerate(CHART_TABS))

THEME_HEAD = r"""<script>try{var t=localStorage.getItem('codex-theme');if(t==='dark'){document.documentElement.setAttribute('data-theme','dark');}}catch(e){}</script>"""
TOTAL_BLOCKS = BLOCK_BUDGET
HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>The Woodblock Codex | FFXIV Frontline, unabridged</title>
<meta name="description" content="The complete FFXIV Frontline archive: mechanics, five maps, jobs, doctrine, the fourteen named plays, command and bilingual macros. Nothing summarised.">
{CSS}
{THEME_HEAD}
</head>
<body>
<div class="progress" aria-hidden="true"></div>
<button class="theme-toggle" id="themeToggle" type="button" aria-pressed="false" aria-label="Switch to dark theme"><span class="sw" aria-hidden="true"></span><span id="themeLabel">Dark theme</span></button>

<header class="hero">
  <canvas class="hero-ink" id="inkCanvas" aria-hidden="true"></canvas>
  <div class="seigaiha" aria-hidden="true"></div>
  <div class="shell hero-inner">
    {SEAL_SVG}
    <p class="seal"><b></b>Frontline, complete and unabridged</p>
    <h1 class="title">The Woodblock <em>Codex</em></h1>
    <p class="lede">Every mechanic, every map, every job, every named play, every macro and every citation,
      set down whole. Nothing here is compressed, and nothing has been left out.</p>
    <div class="hero-meta">
      <div>Documents<b>7</b></div>
      <div>Blocks of knowledge<b data-count="{TOTAL_BLOCKS}">{TOTAL_BLOCKS}</b></div>
      <div>Charts<b>6</b></div>
      <div>Maps covered<b>5</b></div>
      <div>Jobs profiled<b>21</b></div>
    </div>
    <div class="cta-row">
      <a class="cta-open" href="#dash">Open the numbers<i></i></a>
      <a class="cta-quiet" href="#doc-0">Read the whole archive</a>
    </div>
  </div>
</header>

<div class="shell layout">
  <nav class="rail rise" aria-label="Codex index">
    <p class="rail-h">Codex index</p>
    <input class="filter" id="railFilter" type="search" placeholder="Filter contents" aria-label="Filter the codex index">
    {TOC_HTML}
  </nav>

  <main>
    <section class="sec rise" id="dash">
      <div class="sec-head"><span class="sec-num">01</span>
        <div><h2 class="sec-t">The numbers, drawn</h2>
        <p class="sec-sub">Six charts carry the whole economy of a campaign: what wins, what it pays,
          and what a death costs.</p></div></div>
      <div class="dash" data-tabs>
        <div class="tabs" role="tablist" aria-label="Charts">{TABS_HTML}</div>
        <div>{PANELS_HTML}</div>
      </div>
    </section>

    <section class="sec rise">
      <div class="sec-head"><span class="sec-num">02</span>
        <div><h2 class="sec-t">Role actions, at a glance</h2>
        <p class="sec-sub">Every role equips exactly one of three. This is the whole menu, and the pick
          that matters in each row.</p></div></div>
      <div class="panel">{ROLE_ROWS}</div>
    </section>

    <section class="sec rise" id="archive">
      <div class="sec-head"><span class="sec-num">03</span>
        <div><h2 class="sec-t">The archive</h2>
        <p class="sec-sub">Seven documents, {TOTAL_BLOCKS} blocks, in full. Tables stay tables;
          the citations stay attached.</p></div></div>
      {"".join(body)}
    </section>

    <footer>
      <div class="foot-row">
        <span>The Woodblock Codex. Reference patch 7.5.</span>
        <span>{TOTAL_BLOCKS} blocks &middot; 7 documents &middot; 5 maps &middot; 21 jobs.</span>
      </div>
    </footer>
  </main>
</div>
{JS}
</body>
</html>
"""

(OUT / "index.html").write_text(HTML, encoding="utf-8")
print("wrote", OUT / "index.html", len(HTML), "bytes;", TOTAL_BLOCKS, "blocks;",
      sum(len(t["subs"]) for t in toc), "toc entries")
