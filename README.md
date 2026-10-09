# Frontline Sites

Two self-contained FFXIV Frontline reference sites. Each is a single HTML file
with every asset inlined (art is inline SVG and canvas, charts are hand-drawn
SVG, type is system fonts), so they open by double-click with no server, no CDN
and no network. The information is also stored as markdown in `sources/`, so the
sites can be regenerated and the knowledge survives without them.

## The two sites

| Folder | Site | What it is |
|---|---|---|
| `woodblock-codex/` | **The Woodblock Codex** | The unabridged archive. Every mechanic, all five maps, all 21 jobs, the 14 named plays, the 27 bilingual callouts and every citation. 7 documents, roughly 166,000 characters, 51 tables, 27 copy-ready macro blocks. |
| `plotting-table/` | **The Plotting Table** | The briefing. Eight plates: five levers, the numbers, the five maps, the roster, the kill chain, the 14 plays, the call sheet, the quick reference. Roughly 10,000 characters. |

Open either `index.html` directly, or via `file:///` in a browser.

## Design

Both sites are hand-built; no generated imagery, no stock art, no template.

- **Woodblock Codex** is paper and iron-gall ink: cool paper `#f2f1ec`, ink
  `#16181a`, a single vermilion `#d5432a` seal, serif editorial type, a drifting
  ink-wash canvas and a seal that draws itself on load.
- **Plotting Table** is graphite and chalk: ground `#14161a`, ink `#e9edf0`, a
  single chartreuse `#c6f24e` signal, mono-forward type, a radar sweep and
  drifting contour lines.

Charts animate their line draw on reveal. Motion is suppressed under
`prefers-reduced-motion` and a 2.5 second safety net reveals everything
regardless, so no content can be left invisible.

## Verified, not asserted

Both pages were measured in headless Chrome over CDP (`tools/measure.mjs`,
`tools/verify.mjs`), not eyeballed:

| | Woodblock Codex | Plotting Table |
|---|---|---|
| Horizontal overflow | none | none |
| Visible text | ~166,000 chars | ~10,000 chars |
| Tables / rows | 51 / 441 | none (chart-led) |
| Code blocks with copy buttons | 27 | none |
| Chart path widths | 633 to 636 px | 960 to 974 px |
| Content left hidden by animation | 0 | 0 |
| JavaScript errors | 0 | 0 |

The codex's fidelity is separately proven by counting: the parser reports
163/163 headings, 451/451 bullets, 51 tables and 27/27 code blocks against the
sources, with zero mismatch.

## Regenerating the sites

Requires Python 3 only (no third-party packages) for the build, and Node plus a
Chrome or Edge binary for the verification harness.

```bash
python tools/md2blocks.py     # sources/*.md  ->  _build/content.json (+ coverage report)
python tools/site_a.py        # -> woodblock-codex/index.html
python tools/site_b.py        # -> plotting-table/index.html
node  tools/verify.mjs        # measures both pages, rewrites the previews
```

Set `CHROME_BIN` if your browser is not at one of the usual paths. The verifier
needs nothing installed beyond Node, since it talks to the browser over the
DevTools protocol using Node's built-in WebSocket.

## Sources

`sources/` holds the seven documents the codex renders (01 to 07). The reference
figures come from the Lodestone patch notes and the in-game Frontline Campaign
Info panel, cross-checked against consolegameswiki, Japanese practitioner
write-ups and the community tier lists; the pages cite their sources inline.

Reference patch: **7.5**. Re-verify after any major PvP patch.

## Note on the earlier versions

An earlier pair of Frontline sites was hosted on Higgsfield. Those are
superseded by these two and are no longer maintained.
