#!/usr/bin/env python3
"""Builds the summarised site: 'The Plotting Table'.

Graphite and chalk with a single chartreuse signal. Mono-forward, telemetry
framing, six charts. Everything inline: no CDN, no external asset, no host gate.
"""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "plotting-table"
OUT.mkdir(parents=True, exist_ok=True)

# ----------------------------------------------------------------- facts used
THRESH = [("Onsal Hakair", 1400, "Danshig Naadam"), ("Worqor Chirteh", 1400, "Triumph"),
          ("Fields of Glory", 1600, "Shatter"), ("Seal Rock", 2000, "Seize"),
          ("Borderland Ruins", 2400, "Secure")]
NODE_TICK = [2, 4, 6, 10, 12, 14, 18, 20, 22]
OVOO_DECAY = [(30, 200), (20, 120), (15, 100), (10, 60), (6, 40)]
BH_KO = [4, 6, 8, 12, 16, 20]
PHASES = [("00:00 to 04:00", "Asymmetric and cautious", "Farm Battle High on stragglers. Take the safe objective. Never commit the reserve."),
          ("04:00 to 14:00", "Mass and pivot", "Hold the interior position. Contest the centre only as a two against the leader."),
          ("14:00 to 20:00", "Rate, not risk", "Leading: accumulate quietly, take no open melee. Behind: force the leader to split.")]

LEVERS = [
    ("01", "One voice", "A shot-caller turns twenty-four players into one instrument. Six people typing six plans is the default way to lose."),
    ("02", "One mass", "Fight as a single body, never three groups of eight. Combat power scales with the square of numbers, so two groups of twelve lose to one of twenty-four."),
    ("03", "Battle High first", "It multiplies damage and healing by up to fifty per cent and it converts straight into score on the objective maps. Farm it early on stragglers, protect it late by not dying."),
    ("04", "Play your rank", "First place gets hunted and charges Limit Break a quarter slower. Second and third charge faster. If you lead, stop taking fair fights; if you trail, force them."),
    ("05", "Rotate, do not trickle", "Map open, mounts out, rotate on the timer. Trickling back after a wipe is how a lead becomes a rout."),
]

MAPS = [
    ("Borderland Ruins", "Secure", "2,400", "Nine key locations and the centre Allagan weaponry. Four nodes is the income breakpoint; the value per three seconds climbs from two at one node to twenty-two at nine. Farm the Nodes for a hundred and fifty, and never fight on the teleport pad edges."),
    ("Seal Rock", "Seize", "2,000 data", "Allagan tomeliths, and they can be stolen. Win the fight at the tomelith, then channel: any hit interrupts. A knockout both adds your data and subtracts theirs."),
    ("Fields of Glory", "Shatter", "1,600 data", "Damage to icebound tomeliths is the score, so Battle High is literally currency here. Small ice caps at fifty, large at two hundred, split by damage share. Small ice always activates at 12:30 and 4:30 remaining."),
    ("Onsal Hakair", "Danshig Naadam", "1,400", "Ovoos cannot be stolen, only interrupted. It is a race, not a defence. Claim what you can complete, and break the claim the leader needs with a single ranged hit."),
    ("Worqor Chirteh", "Triumph", "1,400", "Every field around a triumph must be held, one player each, and any enemy inside blocks the capture. Snow arrives at about 16:00, auroras at about 9:00, and auroras raise both the ranks and everybody's Limit Break."),
]

ROLES = [
    ("Tank", "Paladin, Warrior, Dark Knight, Gunbreaker", "Rampage, Rampart or Full Swing", "Rampage is the pick on almost every tank: eight thousand potency and twenty-five per cent more damage taken on everything nearby."),
    ("Healer", "White Mage, Scholar, Astrologian, Sage", "Haelan, Stoneskin II or Diabrosis", "Diabrosis is unanimous. Thirty-three per cent less healing received is the only reliable answer to a good healer."),
    ("Melee", "Monk, Dragoon, Ninja, Samurai, Reaper, Viper", "Bloodbath, Swift or Smite", "Smite ignores Guard and its cooldown resets on every knockout. It is the best cleanup tool in the mode."),
    ("Physical ranged", "Bard, Machinist, Dancer", "Dervish, Bravery or Eagle Eye", "Bravery gives twenty-five per cent more damage dealt and twenty-five per cent less taken for fifteen seconds on a thirty second cooldown."),
    ("Magical ranged", "Black Mage, Summoner, Red Mage, Pictomancer", "Comet, Phantom Dart or Rust", "Phantom Dart adds twenty-five per cent damage taken on a fifteen second cooldown. On Shatter it is the ice-breaking button."),
]

JOB_ONE_LINERS = [
    ("Paladin", "The highest burst in the game wearing plate. Think of it as a melee, not a tank."),
    ("Warrior", "The forgiving one. Twenty-second crowd-controlled burst cycle and real self-healing."),
    ("Dark Knight", "The initiator of the mode. Salt Earth is the best pull in Frontline."),
    ("Gunbreaker", "The wall that never falls, carrying the highest total-damage Limit Break."),
    ("White Mage", "The clearest heals and a long-range area stun that decides fights."),
    ("Scholar", "Damage over time and shields. No burst, so it cannot decide a fight."),
    ("Astrologian", "The support that pays for itself: thirty per cent more damage for the whole party."),
    ("Sage", "Not a healer. A twenty-five yalm blink into a pull, with near-melee mitigation."),
    ("Monk", "Meteor Drive strips defence and locks the target. The best catch tool there is."),
    ("Dragoon", "The strongest area burst in the mode and unmatched mobility, with no crowd control at all."),
    ("Ninja", "The finisher. Nothing kills a half-dead target the way this does."),
    ("Samurai", "Pressure as a job. Any barrier defeats its one-shot, so it waits for you to be careless."),
    ("Reaper", "Seventy per cent one Limit Break, and playing that Limit Break well is the hard part."),
    ("Viper", "The current protagonist: top burst, mobility and durability at once, and no crowd control."),
    ("Bard", "With its role action it out-tanks melee. An advanced job that beginners mistake for simple."),
    ("Machinist", "The executioner. Kills anything already leaving, and the turret denies objectives."),
    ("Dancer", "The best Limit Break in the mode, and the only job rated top on all five maps."),
    ("Black Mage", "Area damage that never stops, and it evaporates the moment its cooldowns are down."),
    ("Summoner", "Bahamut's range is enormous and the Limit Break is easy. It has no escape skill at all."),
    ("Red Mage", "Fights in melee on purpose with forty-five per cent damage taken, and silences groups."),
    ("Pictomancer", "Damage that does not depend on the Limit Break, with a blink and a speed buff."),
]

AFFINITY = [("Paladin", [3, 3, 4, 4, 3]), ("Warrior", [4, 3, 4, 4, 4]), ("Dark Knight", [4, 4, 3, 3, 4]),
            ("Gunbreaker", [4, 3, 3, 3, 3]), ("White Mage", [3, 4, 4, 4, 3]), ("Scholar", [1, 1, 1, 1, 1]),
            ("Astrologian", [3, 4, 4, 4, 3]), ("Sage", [3, 2, 3, 3, 3]), ("Monk", [3, 3, 2, 3, 3]),
            ("Dragoon", [4, 3, 4, 4, 4]), ("Ninja", [3, 3, 3, 3, 4]), ("Samurai", [4, 4, 3, 3, 3]),
            ("Reaper", [4, 4, 4, 3, 4]), ("Viper", [4, 3, 4, 3, 4]), ("Bard", [2, 1, 3, 3, 2]),
            ("Machinist", [2, 2, 3, 3, 2]), ("Dancer", [4, 4, 4, 4, 4]), ("Black Mage", [3, 3, 4, 4, 4]),
            ("Summoner", [3, 4, 3, 3, 3]), ("Red Mage", [3, 2, 4, 4, 3]), ("Pictomancer", [3, 3, 3, 4, 3])]
MAP_ORDER = ["Secure", "Seize", "Shatter", "Naadam", "Triumph"]

CHAIN = [
    ("Initiation", "Put them where they cannot leave", "Dark Knight, Warrior, Sage, Dancer, Reaper, Monk", "Salt Earth pull and bind; Primal Rend stun; Plegma pull; Contra Dance."),
    ("Amplification", "Raise everyone's damage on that target", "Tank, ranged, Astrologian", "Rampage plus twenty-five per cent taken; Phantom Dart plus twenty-five; Astrodyne plus thirty for the party."),
    ("Denial", "Remove the defences that would save them", "Tank, melee, ranged, healer", "Full Swing strips Guard; Smite and Eagle Eye ignore it; Diabrosis cuts healing by a third."),
    ("Sustain", "Keep the dive alive long enough", "Warrior, Paladin, Gunbreaker, Samurai, Viper, healers", "Self-healing, barriers, Bloodbath stealing life back while you commit."),
    ("Finish", "Kill them before help arrives", "Ninja, Samurai, Machinist, Dragoon, Dancer", "Assassinate, Zantetsuken, Magic Bullet, Sky Shatter, Blade Dance."),
]

PLAYS = [
    ("The 4x Rule", "Count before you commit. At one and a half times their numbers, engage. Even numbers, take the objective instead of the fight. Fewer, disengage and delay."),
    ("The Defile", "Outnumbered? Fight where fire cannot concentrate. Corners, ramps, chokepoints and line-of-sight breaks turn the square law back into a straight line."),
    ("Split Forcing", "Objectives are a dispersion machine. Separate twenty-four into twelve and twelve and their combat power falls by half."),
    ("The Schwerpunkt", "One decisive point per phase, with everything on it. Deciding which point, early, is the whole job of the caller."),
    ("The Floating Squad", "Six to eight players never committed. They plug flanks, exploit wins and counter-punch. This is the reserve that makes a plan survive contact."),
    ("The Pivot", "Own the central position and you reach every front first. Interior lines are a positioning habit, not a strategy."),
    ("Trade the Centre for the Ring", "Cede the contested centre and take three mid-tier objectives at once. You lose the argument and win the match."),
    ("The Rear-Ring Raid", "Hit the objectives they think are safe, then leave before the respawns land on you."),
    ("The Anvil and the Hammer", "One third fixes the enemy in place. Two thirds strike the exposed fraction. Never the whole line at once."),
    ("The Ghost Flank", "The enemy's only sensor is the map, and the map shows only what their units can see. Eight riders can read as twenty."),
    ("The Pre-Load", "Be standing on the objective before it activates. The timers are public; use them."),
    ("The Sunk-Cost Strike", "Attack the moment they commit to something else. Force a choice between two losses."),
    ("Break Contact on Victory", "Stop at the objective line. Chasing into ten seconds of respawn invincibility is how a won fight becomes a lost match."),
    ("The Quiet Leader", "As first place, stay unclumped and out of the centre; let the other two bleed each other. As third, create chaos and pinch the leader."),
]

ORDERS = ["REGROUP <place>", "PUSH <objective> NOW", "HOLD", "BAIL", "PINCH INCOMING <dir>", "FLOAT", "NO CHASE"]

# ----------------------------------------------------------------- charts
def line_chart(points, labels=None, w=620, h=210, pad=36, dash=False):
    mx = max(v for _, v in points) or 1
    n = len(points)
    def xy(i, v):
        return pad + i * (w - 2 * pad) / max(1, n - 1), h - pad - (v / mx) * (h - 2 * pad)
    d = " ".join(("M" if i == 0 else "L") + f"{xy(i, v)[0]:.1f},{xy(i, v)[1]:.1f}" for i, (_, v) in enumerate(points))
    grid = "".join(f'<line x1="{pad}" y1="{h - pad - g * (h - 2 * pad) / 4:.1f}" x2="{w - pad}" '
                   f'y2="{h - pad - g * (h - 2 * pad) / 4:.1f}" class="g"/>' for g in range(5))
    dots = "".join(f'<circle cx="{xy(i, v)[0]:.1f}" cy="{xy(i, v)[1]:.1f}" r="3.6" class="d"/>'
                   for i, (_, v) in enumerate(points))
    lab = ""
    if labels:
        step = max(1, n // 7)
        lab = "".join(f'<text x="{xy(i, 0)[0]:.1f}" y="{h - pad + 17}" class="ax">{labels[i]}</text>'
                      for i in range(0, n, step))
    cls = "ln dash" if dash else "ln"
    return (f'<svg class="cs" viewBox="0 0 {w} {h}" role="img" aria-label="chart">{grid}'
            f'<path d="{d}" class="{cls}"/><path d="{d}" class="ln draw"/>{dots}{lab}</svg>')


def bars():
    mx = 2400
    return "".join(
        f'<div class="brow"><span class="bl">{label}<em>{sub}</em></span>'
        f'<span class="bt"><span class="bf" style="--w:{v / mx * 100:.1f}%"></span></span>'
        f'<span class="bv">{v}</span></div>' for label, v, sub in THRESH)


def heatmap():
    out = ['<div class="hm" style="--cols:5"><div class="hmc">Job</div>']
    out += [f'<div class="hmh">{m}</div>' for m in MAP_ORDER]
    for name, vals in AFFINITY:
        out.append(f'<div class="hmn">{name}</div>')
        for i, v in enumerate(vals):
            out.append(f'<div class="hx l{v}" title="{name} on {MAP_ORDER[i]}"></div>')
    out.append("</div>")
    return "".join(out)


CSS = r"""
<style>
:root{
  --ground:#14161a; --panel:#1a1d22; --panel-2:#20242a; --ink:#e9edf0; --muted:#8d949c;
  --faint:#5f666e; --line:#2c3037; --sig:#c6f24e; --warn:#ff7a5c;
  --mono: ui-monospace,"Cascadia Mono","SF Mono",Menlo,Consolas,monospace;
  --sans: ui-sans-serif,system-ui,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  --maxw:1500px;
}
*{box-sizing:border-box}
body{margin:0;background:var(--ground);color:var(--ink);font-family:var(--sans);
  font-size:16.5px;line-height:1.62;-webkit-font-smoothing:antialiased}
::selection{background:var(--sig);color:#14161a}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}
.wrap{max-width:var(--maxw);margin:0 auto;padding:0 26px}
.mono{font-family:var(--mono);font-variant-numeric:tabular-nums}
.prog{position:fixed;top:0;left:0;height:2px;background:var(--sig);width:0;z-index:60}

/* hero */
.hero{position:relative;min-height:92vh;display:flex;align-items:center;overflow:hidden;
  border-bottom:1px solid var(--line)}
#radar{position:absolute;inset:0;width:100%;height:100%;opacity:.55}
.contours{position:absolute;inset:-6% -4%;opacity:.16;animation:drift 48s ease-in-out infinite alternate}
@keyframes drift{from{transform:translate3d(-1.6%,0,0)}to{transform:translate3d(1.6%,-1.2%,0)}}
.hero-in{position:relative;z-index:3;padding:96px 0 72px;width:100%}
.tag{font-family:var(--mono);font-size:11px;letter-spacing:.28em;text-transform:uppercase;
  color:var(--sig);display:flex;align-items:center;gap:12px}
.tag::before{content:"";width:34px;height:1px;background:var(--sig);display:block}
h1{font-family:var(--mono);font-weight:600;text-transform:uppercase;letter-spacing:-.02em;
  font-size:clamp(40px,7.4vw,104px);line-height:.98;margin:26px 0 0}
h1 span{color:var(--sig)}
.sub{max-width:60ch;color:#c4cbd2;font-size:18.5px;margin:24px 0 0}
.readout{display:flex;flex-wrap:wrap;gap:0;margin-top:46px;border-top:1px solid var(--line)}
.readout div{padding:16px 30px 4px 0;margin-right:30px;border-right:1px solid var(--line)}
.readout div:last-child{border-right:0}
.readout b{display:block;font-family:var(--mono);font-size:32px;color:var(--sig);letter-spacing:-.02em}
.readout em{font-style:normal;font-family:var(--mono);font-size:10.5px;letter-spacing:.2em;
  text-transform:uppercase;color:var(--faint)}
.cta{display:flex;gap:16px;flex-wrap:wrap;margin-top:44px}
.b1{font-family:var(--mono);font-size:13px;letter-spacing:.14em;text-transform:uppercase;
  background:var(--sig);color:#14161a;border:0;padding:16px 26px;text-decoration:none;cursor:pointer;
  clip-path:polygon(0 0,calc(100% - 12px) 0,100% 12px,100% 100%,12px 100%,0 calc(100% - 12px));
  transition:transform .16s,background .16s}
.b1:hover{background:#d6ff62;transform:translateY(-1px)}
.b1:active{transform:translateY(0) scale(.99)}
.b2{font-family:var(--mono);font-size:13px;letter-spacing:.14em;text-transform:uppercase;
  background:none;color:var(--ink);border:1px solid var(--line);padding:16px 26px;
  text-decoration:none;cursor:pointer;transition:border-color .16s,color .16s}
.b2:hover{border-color:var(--sig);color:var(--sig)}

/* plates */
.plate{border-top:1px solid var(--line);padding:78px 0}
.phead{display:grid;grid-template-columns:132px minmax(0,1fr);gap:26px;align-items:start;margin-bottom:34px}
@media(max-width:760px){.phead{grid-template-columns:1fr;gap:12px}}
.pid{font-family:var(--mono);font-size:12px;letter-spacing:.2em;color:var(--sig);padding-top:12px}
.ph2{font-size:clamp(27px,3.6vw,46px);font-family:var(--mono);font-weight:600;text-transform:uppercase;
  letter-spacing:-.015em;line-height:1.04;margin:0}
.psub{margin:12px 0 0;color:var(--muted);max-width:74ch}

/* grid bits */
.dash{display:grid;grid-template-columns:212px minmax(0,1fr);gap:0;border:1px solid var(--line)}
@media(max-width:880px){.dash{grid-template-columns:1fr}}
.tabs{display:flex;flex-direction:column;border-right:1px solid var(--line)}
@media(max-width:880px){.tabs{flex-direction:row;flex-wrap:wrap;border-right:0;border-bottom:1px solid var(--line)}}
.tab{background:none;border:0;border-bottom:1px solid var(--line);text-align:left;padding:14px 18px;
  font-family:var(--mono);font-size:11.5px;letter-spacing:.13em;text-transform:uppercase;
  color:var(--muted);cursor:pointer;transition:color .14s,background .14s}
.tab:hover{color:var(--ink);background:#191c21}
.tab[aria-selected="true"]{color:#14161a;background:var(--sig)}
.pan{padding:28px}
.pan[hidden]{display:none}
.pan h3{margin:0 0 6px;font-family:var(--mono);font-size:19px;letter-spacing:-.01em}
.pan p{margin:0 0 20px;color:var(--muted);font-size:14.4px;max-width:76ch}
.cs{width:100%;height:auto;overflow:visible}
.g{stroke:#2c3037;stroke-width:1;stroke-dasharray:3 4}
.ln{fill:none;stroke:var(--ink);stroke-width:2}
.ln.dash{stroke-dasharray:5 5;stroke:var(--faint)}
.ln.draw{stroke:var(--sig);stroke-width:2;stroke-dasharray:1500;stroke-dashoffset:1500}
.in .ln.draw{animation:dr 1.7s cubic-bezier(.5,0,.2,1) forwards}
@keyframes dr{to{stroke-dashoffset:0}}
.d{fill:var(--sig)}
.ax{font-family:var(--mono);font-size:10px;fill:var(--faint);text-anchor:middle}
.brow{display:grid;grid-template-columns:186px 1fr 64px;gap:14px;align-items:center;
  padding:10px 0;border-bottom:1px solid var(--line)}
.bl{font-size:14.6px}
.bl em{display:block;font-style:normal;font-family:var(--mono);font-size:10.5px;color:var(--faint);
  letter-spacing:.14em;text-transform:uppercase}
.bt{height:10px;background:#23272d;position:relative;overflow:hidden}
.bf{position:absolute;inset:0 auto 0 0;width:0;background:var(--sig)}
.in .bf{animation:gw 1.4s cubic-bezier(.4,0,.2,1) forwards;width:var(--w)}
@keyframes gw{from{width:0}to{width:var(--w)}}
.bv{text-align:right;font-family:var(--mono);font-size:14px;color:var(--sig)}
.hm{display:grid;grid-template-columns:118px repeat(var(--cols),minmax(0,1fr));gap:4px}
.hmc,.hmh{font-family:var(--mono);font-size:10px;letter-spacing:.14em;text-transform:uppercase;
  color:var(--faint);text-align:center;padding:4px 0}
.hmc{text-align:left}
.hmn{font-size:12.4px;color:#c4cbd2;padding:4px 6px 4px 0;border-right:1px solid var(--line)}
.hx{aspect-ratio:2.1/1;background:#22262c}
.hx.l1{background:#22262c}.hx.l2{background:#3a4148}.hx.l3{background:#7d8791}.hx.l4{background:var(--sig)}
.hx:hover{outline:1px solid var(--ink);outline-offset:-1px}

/* rows */
.lever,.row{display:grid;gap:20px;padding:22px 0;border-bottom:1px solid var(--line)}
.lever{grid-template-columns:76px minmax(0,1fr)}
.lever .n{font-family:var(--mono);font-size:26px;color:var(--sig);padding-top:2px}
.lever h3{margin:0 0 6px;font-size:20px}
.lever p{margin:0;color:var(--muted);max-width:74ch}
.row{grid-template-columns:210px minmax(0,1fr)}
@media(max-width:760px){.row,.lever{grid-template-columns:1fr}}
.row h3{margin:0 0 4px;font-size:17px}
.row .k{font-family:var(--mono);font-size:10.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--sig)}
.row p{margin:8px 0 0;color:var(--muted);font-size:14.6px;max-width:76ch}
.chain{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:1px;background:var(--line);
  border:1px solid var(--line)}
@media(max-width:1000px){.chain{grid-template-columns:1fr}}
.step{background:var(--panel);padding:24px}
.step .s{font-family:var(--mono);font-size:10.5px;letter-spacing:.2em;color:var(--sig)}
.step h3{margin:12px 0 6px;font-size:18px}
.step p{margin:0 0 12px;color:var(--muted);font-size:14px}
.step .who{font-family:var(--mono);font-size:11.5px;color:#c4cbd2;border-top:1px dashed var(--line);padding-top:10px}
.plays{display:grid;grid-template-columns:repeat(auto-fill,minmax(268px,1fr));gap:1px;background:var(--line);
  border:1px solid var(--line)}
.play{background:var(--panel);border:0;text-align:left;padding:20px;color:var(--ink);cursor:pointer;
  transition:background .16s}
.play:hover{background:var(--panel-2)}
.play .pn{font-family:var(--mono);font-size:10.5px;color:var(--faint);letter-spacing:.16em}
.play h3{margin:8px 0 0;font-size:16.5px}
.play p{margin:10px 0 0;color:var(--muted);font-size:14px;display:none}
.play.open p{display:block}
.play.open{box-shadow:inset 3px 0 0 var(--sig)}
.orders{display:flex;flex-wrap:wrap;gap:10px;margin:22px 0 0}
.orders span{font-family:var(--mono);font-size:12px;letter-spacing:.08em;border:1px solid var(--line);
  padding:8px 12px;color:#c4cbd2}
.quick{display:grid;grid-template-columns:repeat(auto-fill,minmax(232px,1fr));gap:1px;background:var(--line);
  border:1px solid var(--line)}
.q{background:var(--panel);padding:20px}
.q b{display:block;font-family:var(--mono);font-size:25px;color:var(--sig);letter-spacing:-.02em}
.q em{font-style:normal;display:block;font-family:var(--mono);font-size:10px;letter-spacing:.18em;
  text-transform:uppercase;color:var(--faint);margin-bottom:9px}
.q p{margin:8px 0 0;color:var(--muted);font-size:13.6px}
footer{border-top:1px solid var(--line);padding:40px 0 64px;color:var(--faint);
  font-family:var(--mono);font-size:11.5px;letter-spacing:.1em;display:flex;justify-content:space-between;
  flex-wrap:wrap;gap:16px}
.rise{opacity:1;transform:none}
html.mo .rise{opacity:0;transform:translateY(18px)}
html.mo .rise.in{opacity:1;transform:none;transition:opacity .55s ease,transform .55s cubic-bezier(.2,.7,.2,1)}
@media(prefers-reduced-motion:reduce){
  html.mo .rise{opacity:1;transform:none}
  .in .bf{animation:none;width:var(--w)} .in .ln.draw{animation:none;stroke-dashoffset:0}
}
</style>
"""

JS = r"""
<script>
(function(){
  var html=document.documentElement;
  var reduce=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if(!reduce){html.classList.add('mo');}
  var bar=document.querySelector('.prog');
  function tick(){var h=document.documentElement.scrollHeight-innerHeight;
    bar.style.width=(h>0?scrollY/h*100:0)+'%';}
  addEventListener('scroll',tick,{passive:true});tick();
  var items=[].slice.call(document.querySelectorAll('.rise,.plate,.pan'));
  function show(e){e.classList.add('in');}
  if(!reduce&&'IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){es.forEach(function(e){
      if(e.isIntersecting){show(e.target);io.unobserve(e.target);}});},{rootMargin:'0px 0px -6% 0px'});
    items.forEach(function(e){io.observe(e);});
    setTimeout(function(){items.forEach(show);},2500);
  } else { items.forEach(show); }

  [].slice.call(document.querySelectorAll('[data-tabs]')).forEach(function(g){
    var tabs=[].slice.call(g.querySelectorAll('[role=tab]'));
    tabs.forEach(function(t){t.addEventListener('click',function(){
      tabs.forEach(function(x){x.setAttribute('aria-selected',x===t?'true':'false');
        var p=document.getElementById(x.getAttribute('aria-controls'));if(p){p.hidden=(x!==t);}});
      var a=document.getElementById(t.getAttribute('aria-controls'));if(a){a.classList.add('in');}
    });});
  });

  document.addEventListener('click',function(e){
    var p=e.target.closest&&e.target.closest('.play'); if(!p)return;
    p.classList.toggle('open');
  });

  /* plotting-table sweep */
  var cv=document.getElementById('radar');
  if(cv&&!reduce){
    var x=cv.getContext('2d'),W,H,ang=0;
    function size(){W=cv.width=cv.offsetWidth;H=cv.height=cv.offsetHeight;}
    size();addEventListener('resize',size);
    var blips=[[0.28,0.34],[0.62,0.22],[0.71,0.58],[0.42,0.77],[0.55,0.45],[0.33,0.61]];
    (function loop(){
      x.clearRect(0,0,W,H);
      var cx=W*0.72,cy=H*0.5,R=Math.min(W,H)*0.62;
      x.strokeStyle='rgba(198,242,78,0.22)';x.lineWidth=1.2;
      for(var i=1;i<=4;i++){x.beginPath();x.arc(cx,cy,R*i/4,0,6.284);x.stroke();}
      x.strokeStyle='rgba(233,237,240,0.13)';
      for(var k=1;k<=6;k++){x.beginPath();x.arc(cx,cy,R*(k/7.5),0,6.284);x.stroke();}
      x.setLineDash([5,8]);
      x.beginPath();x.moveTo(cx-R,cy);x.lineTo(cx+R,cy);x.moveTo(cx,cy-R);x.lineTo(cx,cy+R);x.stroke();
      x.setLineDash([]);
      var g=x.createConicGradient?null:null;
      x.save();x.translate(cx,cy);x.rotate(ang);
      var grad=x.createLinearGradient(0,0,R,0);
      grad.addColorStop(0,'rgba(198,242,78,0.46)');grad.addColorStop(1,'rgba(198,242,78,0)');
      x.fillStyle=grad;x.beginPath();x.moveTo(0,0);x.arc(0,0,R,-0.40,0);x.closePath();x.fill();
      x.strokeStyle='rgba(198,242,78,0.75)';x.beginPath();x.moveTo(0,0);x.lineTo(R,0);x.stroke();
      x.strokeStyle='rgba(198,242,78,0.30)';x.lineWidth=6;x.beginPath();x.moveTo(0,0);x.lineTo(R,0);x.stroke();
      x.restore();
      blips.forEach(function(b,i){
        var a=Math.atan2(b[1]-0.5,b[0]-0.72);var d=Math.hypot(b[0]-0.72,b[1]-0.5)*R/0.62;
        var diff=((a-ang)%6.284+6.284)%6.284;var glow=Math.max(0,1-diff/1.5);
        x.fillStyle='rgba(198,242,78,'+(0.26+glow*0.74)+')';
        x.beginPath();x.arc(W*b[0],H*b[1],2.6+glow*3.2,0,6.284);x.fill();
      });
      ang+=0.0055;requestAnimationFrame(loop);
    })();
  }
})();
</script>
"""

CONTOUR = """
<svg class="contours" viewBox="0 0 1440 900" preserveAspectRatio="none" aria-hidden="true">
  <g fill="none" stroke="#e9edf0" stroke-width="1">
    <path d="M-40 620C180 520 300 700 520 610S860 430 1080 560s300 40 420-30"/>
    <path d="M-40 700C180 600 300 780 520 690S860 510 1080 640s300 40 420-30"/>
    <path d="M-40 780C180 680 300 860 520 770S860 590 1080 720s300 40 420-30"/>
    <path d="M-40 540C180 440 300 620 520 530S860 350 1080 480s300 40 420-30"/>
    <path d="M-40 460C180 360 300 540 520 450S860 270 1080 400s300 40 420-30"/>
  </g>
</svg>"""

LEVERS_HTML = "".join(
    f'<div class="lever rise"><span class="n">{n}</span><div><h3>{t}</h3><p>{d}</p></div></div>'
    for n, t, d in LEVERS)
MAPS_HTML = "".join(
    f'<div class="row rise"><div><span class="k">{mode}</span><h3>{name}</h3>'
    f'<p class="mono" style="color:var(--sig);margin:6px 0 0">{target}</p></div><p>{desc}</p></div>'
    for name, mode, target, desc in MAPS)
ROLES_HTML = "".join(
    f'<div class="row rise"><div><span class="k">{role}</span><h3>{jobs}</h3>'
    f'<p class="mono" style="color:#c4cbd2;margin:6px 0 0">{acts}</p></div><p>{note}</p></div>'
    for role, jobs, acts, note in ROLES)
JOBS_HTML = "".join(
    f'<div class="row rise"><div><h3>{j}</h3></div><p>{d}</p></div>' for j, d in JOB_ONE_LINERS)
CHAIN_HTML = "".join(
    f'<div class="step"><span class="s">{i + 1} / 5</span><h3>{name}</h3><p>{what}</p>'
    f'<div class="who">{who}<br>{tools}</div></div>'
    for i, (name, what, who, tools) in enumerate(CHAIN))
PLAYS_HTML = "".join(
    f'<button class="play rise" type="button"><span class="pn">PLAY {i + 1:02d}</span>'
    f'<h3>{n}</h3><p>{d}</p></button>' for i, (n, d) in enumerate(PLAYS))
ORDERS_HTML = "".join(f"<span>{o}</span>" for o in ORDERS)

CHART_TABS = [
    ("t", "Win thresholds", f'<div class="bars">{bars()}</div>',
     "Every campaign is a threshold, never a kill count. The number on the left is the objective."),
    ("n", "Secure node income", line_chart([(i + 1, v) for i, v in enumerate(NODE_TICK)],
                                           labels=[str(i + 1) for i in range(9)]),
     "Tactical rating per three seconds by key locations held. Four nodes is the breakpoint."),
    ("o", "Ovoo payout decay", line_chart(OVOO_DECAY, labels=[f"{s}s" for s, _ in OVOO_DECAY], w=560, h=195),
     "An ovoo pays for thirty seconds. If the match ends early you keep only the ticks that landed."),
    ("l", "Lanchester, square against linear", line_chart([(n, n * n) for n in range(1, 9)],
                                                          labels=[str(n) for n in range(1, 9)], w=560, h=195),
     "Aimed fire scales combat power with the square of numbers. Double the side and you quadruple the power."),
    ("h", "Job by map affinity", heatmap(),
     "Twenty-one jobs against five maps. Bright cells are where the job is worth playing."),
]
TABS_HTML = "".join(
    f'<button class="tab" role="tab" aria-selected="{"true" if i == 0 else "false"}" '
    f'aria-controls="pan-{cid}">{label}</button>' for i, (cid, label, _, _) in enumerate(CHART_TABS))
PANS_HTML = "".join(
    f'<div class="pan" id="pan-{cid}" role="tabpanel"{" hidden" if i else ""}>'
    f'<h3>{label}</h3><p>{desc}</p>{body}</div>' for i, (cid, label, body, desc) in enumerate(CHART_TABS))
PHASES_HTML = "".join(
    f'<div class="q"><em>{when}</em><b>{name}</b><p>{what}</p></div>' for when, name, what in PHASES)

HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>The Plotting Table | FFXIV Frontline, the briefing</title>
<meta name="description" content="The FFXIV Frontline briefing: five levers, the numbers, the five maps, the job roster, the kill chain, fourteen named plays and the call sheet.">
{CSS}
</head>
<body>
<div class="prog" aria-hidden="true"></div>

<header class="hero">
  <canvas id="radar" aria-hidden="true"></canvas>
  {CONTOUR}
  <div class="wrap hero-in">
    <p class="tag">Frontline 7.5 &middot; the briefing</p>
    <h1>The Plotting <span>Table</span></h1>
    <p class="sub">Everything that decides a Frontline match, laid out the way a commander reads it:
      five levers, the numbers, five maps, the roster, the chain, fourteen plays and the call sheet.</p>
    <div class="readout">
      <div><b data-count="72">72</b><em>Players</em></div>
      <div><b data-count="24">24</b><em>Per team</em></div>
      <div><b data-count="20">20</b><em>Minutes</em></div>
      <div><b data-count="5">5</b><em>Maps</em></div>
      <div><b data-count="21">21</b><em>Jobs</em></div>
      <div><b data-count="14">14</b><em>Named plays</em></div>
    </div>
    <div class="cta">
      <a class="b1" href="#p1">Enter the briefing</a>
      <a class="b2" href="#p8">Jump to the numbers</a>
    </div>
  </div>
</header>

<main>
  <section class="plate" id="p1">
    <div class="wrap">
      <div class="phead"><span class="pid">01 / LEVERS</span>
        <div><h2 class="ph2">Five levers that move win rate</h2>
        <p class="psub">Job choice moves a match by a few per cent. These five move it by a lot, and all
          five are decisions rather than mechanics.</p></div></div>
      {LEVERS_HTML}
    </div>
  </section>

  <section class="plate" id="p2">
    <div class="wrap">
      <div class="phead"><span class="pid">02 / NUMBERS</span>
        <div><h2 class="ph2">The numbers that decide it</h2>
        <p class="psub">Thresholds, the ovoo payout, node income, Battle High and the square law.
          Every figure re-verified against the patch notes.</p></div></div>
      <div class="dash" data-tabs>
        <div class="tabs" role="tablist" aria-label="Charts">{TABS_HTML}</div>
        <div>{PANS_HTML}</div>
      </div>
    </div>
  </section>

  <section class="plate" id="p3">
    <div class="wrap">
      <div class="phead"><span class="pid">03 / GROUND</span>
        <div><h2 class="ph2">The five maps</h2>
        <p class="psub">Five grounds, five win conditions, and the one thing that wins each of them.</p></div></div>
      {MAPS_HTML}
    </div>
  </section>

  <section class="plate" id="p4">
    <div class="wrap">
      <div class="phead"><span class="pid">04 / ROSTER</span>
        <div><h2 class="ph2">The job roster</h2>
        <p class="psub">Five roles, twenty-one jobs, one role action each. The role decides your role
          action and your damage taken, not your job on the field.</p></div></div>
      {ROLES_HTML}
      <div style="margin-top:44px">{JOBS_HTML}</div>
    </div>
  </section>

  <section class="plate" id="p5">
    <div class="wrap">
      <div class="phead"><span class="pid">05 / CHAIN</span>
        <div><h2 class="ph2">The kill chain</h2>
        <p class="psub">A kill is five stages. Find the missing stage and you have found why you are losing.</p></div></div>
      <div class="chain">{CHAIN_HTML}</div>
    </div>
  </section>

  <section class="plate" id="p6">
    <div class="wrap">
      <div class="phead"><span class="pid">06 / PLAYS</span>
        <div><h2 class="ph2">The fourteen named plays</h2>
        <p class="psub">Doctrine compressed into named moves. Tap any play to open it.</p></div></div>
      <div class="plays">{PLAYS_HTML}</div>
    </div>
  </section>

  <section class="plate" id="p7">
    <div class="wrap">
      <div class="phead"><span class="pid">07 / CALL SHEET</span>
        <div><h2 class="ph2">The call sheet</h2>
        <p class="psub">One caller, two mounted scouts, a main body of fourteen to sixteen, and a floating
          squad of six to eight that is never committed.</p></div></div>
      <div class="row rise"><div><span class="k">Count first</span><h3>Rules of engagement</h3></div>
        <p>One: count before committing. Two: at one and a half times their numbers, engage fully.
        Three: even numbers, take the objective instead of the fight. Four: fewer, bait and delay toward
        allies and find a defile. Five: won, stop, remount, take the objective, do not pursue. Six: losing,
        do not reinforce the wipe, redeploy.</p></div>
      <div class="orders">{ORDERS_HTML}</div>
    </div>
  </section>

  <section class="plate" id="p8">
    <div class="wrap">
      <div class="phead"><span class="pid">08 / REFERENCE</span>
        <div><h2 class="ph2">Quick reference</h2>
        <p class="psub">The whole briefing on one screen: the posture by phase, and the numbers worth
          remembering before the gate opens.</p></div></div>
      <div class="quick">{PHASES_HTML}</div>
      <div class="quick" style="margin-top:1px">
        <div class="q"><em>Kill and death, Naadam</em><b>8 / 8</b><p>A knockout is eight, a death is eight.
          Sixteen points of swing, flat, not scaled by Battle High.</p></div>
        <div class="q"><em>Ovoo, by rank</em><b>50 / 100 / 200</b><p>Paid at five, ten and twenty per three
          seconds across a thirty second window.</p></div>
        <div class="q"><em>Battle High</em><b>100</b><p>Plus ten per cent damage and healing for every twenty
          points. Changing job resets it to zero.</p></div>
        <div class="q"><em>Limit Break charge</em><b>25%</b><p>First place charges a quarter slower, third
          place a quarter faster.</p></div>
      </div>
    </div>
  </section>
</main>

<footer class="wrap">
  <span>The Plotting Table &middot; reference patch 7.5</span>
  <span>The full archive is the companion volume.</span>
</footer>
{JS}
</body>
</html>
"""

(OUT / "index.html").write_text(HTML, encoding="utf-8")
print("wrote", OUT / "index.html", len(HTML), "bytes")
