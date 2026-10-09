---
name: ffxiv-frontline
description: Use when asked FFXIV Frontline PvP strategy or mechanics.
version: 1.1.0
author: DalamudTranslator
license: MIT
metadata:
  hermes:
    tags: [ffxiv, pvp, frontline, strategy, military-doctrine]
    related_skills: [ffxiv-chat-translation]
    editorial_name: FFXIV Frontline
    editorial_description: Frontline PvP strategy — per-map win conditions, verified mechanics numbers, military-doctrine plays, command structure.
---

# FFXIV Frontline

Scope: the 24v24v24 Grand Company battleground — strategy, map playbooks, mechanics numbers, and command structure. Not Crystalline Conflict (4v4) or Rival Wings.

**Live tool:** `FrontlineAdvisor` (`D:\XIVPlugins Self\FrontlineAdvisor`) is a Dalamud plugin built on this doctrine — it reads the game's own Frontline score board and calls the leader, the focus target (the imminent winner), the emerging threat (fastest scorer) and every lead change. Its advice strings ARE this guide's doctrine; keep them in step when the doctrine changes.

**Canonical artifacts:** the full unabridged write-up lives in the shared vault at
`C:/ObsidianVaults/Notebook/Agents/ffxiv/guides/` — `ffxiv-frontline-complete-guide.md` (mechanics, the five maps, doctrine, the 14 plays), `ffxiv-frontline-jobs.md` (roles, role actions, the kill chain, 21 job profiles, map affinity), `ffxiv-frontline-macros.md` and `ffxiv-frontline-call-sheet.md`.
Reproduce from those files rather than re-researching; they are the shareable versions with every table and citation. **The vault is canonical**, and the user also keeps a flat reading copy at `D:/FFXIV Frontline/` with its own README index — that copy is a **snapshot taken at export time**, so refresh it when a guide changes, and describe it as a snapshot rather than implying it tracks.

## When to Use

User asks for Frontline strategy, how to win, map tips, meta/job advice, or "why do I keep losing". Deliver:
1. the mechanics that decide the match (numbers, below),
2. the map playbook,
3. doctrine-derived plays (references/military-doctrine.md),
4. the call sheet and rules of engagement.

## Research pitfall — read first

A web search for "Frontline strategy" returns **World of Tanks' Frontline** (tanks, artillery strikes, pillboxes, hull-down play) as a top result. It is a different game entirely. Filter it out; only FFXIV sources are usable.

Authoritative sources, in order: **Lodestone patch notes** (the only source that settles a changed number), consolegameswiki pages (rules and scoring tables, read with the caveat below), **Japanese practitioner write-ups** (uwasablog.com 「うわさの調べ」 per-role and per-job series, the `note.com` Frontline commander analyses, 5ch threads — deepest and most current on numbers and matchups), then English strategy sites and r/ffxiv threads for meta.

**How to settle a disputed number.** Values move between patches and the English sources do not all follow: the wiki will sometimes **drop a figure entirely** rather than update it, while community posts keep repeating the old one. Settle it from the **patch-note chain** — Naadam 1,800 → 1,600 (5.18) → **1,400** (6.4); Seize data 1,600 → **2,000** (6.4); Naadam KO/death 10 → **8** (5.18) — and tell the user the in-game Frontline Campaign Info panel is the final authority. **Prefer a JP practitioner with a disclosed match count over an English tier list or a boosting-service page:** those lists read as SEO content and rate jobs for coordinated pre-made play, which contradicts solo queue (they rank Scholar top tier; practitioners say its damage cannot decide a fight).

**Re-verify after every major PvP patch.** Balance-sensitive items: Battle High behaviour on death, job damage-taken modifiers, rating thresholds per map, role-action lists. Patch 7.5 = no Battle High loss on death; patch 7.2 = Secure rework + role actions.

## Core mechanics (verified reference)

- 24 per team, 72 total, 20-minute limit, random Grand Company, premade **max 4**.
- Win condition is a **rating threshold**, never kill count. Most matches decided by rating, not the clock.
- Leaving the landing platform grants **10s Invincibility**; respawns come back **at the platform**.
- Any hit **dismounts** you and applies **Hoofing It**, which **Purify cannot cleanse**. Dismount voluntarily before contact.
- **The map shows enemy players only within sight range of your own units.** Absence of enemy triangles = unknown, not safe. This is the main information asymmetry in the mode and the basis of the deception plays.

### Battle High

Max 100; **every 20 points = +10% damage dealt and healing potency** (BH V = +50%). BH V is announced to the whole match — expect focus. **Death no longer reduces it (patch 7.5).** **Changing jobs resets it to zero** — the most common self-inflicted loss of a match.

Gain depends on the *victim's* tier: KO 4/6/8/12/16/20, assist 2/3/4/6/8/10 (none / BH I / II / III / IV / V).

### Rubber banding

1st place charges Limit Break **25% slower**, 3rd place **25% faster**. The game hands the losing team tempo — spend it on the leader.

### Survivability (job damage taken)

| | Jobs |
|---|---|
| Soaks −50% to −55% | Warrior, Gunbreaker, Monk, Samurai, Viper |
| Soaks −40% to −45% | Paladin, Dark Knight, Ninja, Dragoon, Reaper, Red Mage |
| Soaks only −25% to −35% | Bard, Machinist, Dancer, Black Mage, Summoner, Pictomancer, White Mage, Scholar, Astrologian, Sage |

Read as a survival ranking. A BLM/WHM/AST caught in the open is a free kill; a WAR/GNB/MNK/SAM is not. Many jobs also take a damage-dealt penalty (−5% to −15%) — casters and healers pay twice.

**The role is not the job.** The role decides exactly two things: which role action you may equip, and your damage-taken modifier. Frontline *function* frequently contradicts the label — **Paladin is a burst DPS** (the highest instantaneous burst in the game; 45% damage taken is shallow for a melee), **Sage is a pull-and-burst assassin, not a healer**, **Scholar contributes little to a burst-decided fight**, **Bard with Bravery out-tanks most melee**, **Red Mage deliberately fights in melee range**. Never advise by role label; advise by function.

### Role Actions (7.2+, one of three per role, set in PvP Profile)

- Tank — **Rampage** (AoE, target +25% damage taken), **Rampart** (−50% taken, +25% healing received), **Full Swing** (30-yalm knockback, strips Guard — the Secure ledge punt).
- Melee — **Bloodbath**, **Swift** (100% movement + full CC/knockback immunity 4s), **Smite** (scales up to 18k on low HP; **recast resets on kill or assist**).
- Healer — **Haelan**, **Stoneskin II** (15-yalm ally barrier), **Diabrosis** (9k AoE, **−33% healing received** — the anti-healer button).
- Physical ranged — **Dervish** (party −10% cast/recast, +33% movement, crosses cover), **Bravery** (**+25% damage dealt AND −25% damage taken**, 15s, **30s recast** — the single strongest role action in the mode), **Eagle Eye Shot** (12k, ignores Guard, 40 yalms).
- Magical ranged — **Comet** (20k AoE, 2.4s cast you cannot move or cancel), **Phantom Dart** (+25% damage taken on the target, 15s recast — take it on Shatter for ice), **Rust** (−33% damage dealt *and* healing on target + nearby).

Community picks per job: tanks **Rampage** (Rampart on DRK/GNB) · melee **Smite** (Bloodbath on DRG/SAM, **Swift on Reaper**) · healers **Diabrosis** unanimously · physical ranged **Bravery** · casters **Phantom Dart** or **Comet**.

**Three outliers:** Bravery (LB-grade effects on a 30s recast), Rampage (+25% damage taken, 45s), Smite (ignores Guard, **recast resets on every KO or assist** — the best cleanup tool in the mode).

### Thresholds and timers

| Map | Target | Key numbers |
|---|---|---|
| Secure | 2,400 rating | 9 nodes; **4 nodes = the income breakpoint**; Nodes +150, α drones +30, Command Systems +24, drones +10, KO +10, death −10 |
| Seize | **700 Data** (lowered from 800 in 6.4) | **Four tomeliths activate 30 seconds in**, then activation follows extraction (**a drained one is replaced about 15 s later**); full extraction takes ~2 min and B/A/S pay **80/120/160**; the map thins out and rank rises as the match runs; **stealable**, channel interrupted by any hit |
| Shatter | 1,600 Data (6.4 raised it to 2,000; 6.57 put it back) | KO = +8 data; small ice caps 50 (300k HP), large caps 200 (3M HP); **a forecast icon shows 30 s before any ice activates**; four map states (gone / black / outlined / blue); first ice damageable ~15 to 30 s in, two large at a time; small-ice waves at **12:30 and 4:30**; official 6.55 timers: first small activation **420 s**, reactivation **420 s**, destroyed small reappears **360 s**, destroyed large respawns **60 s**, max active **15 small / 2 large** |
| Danshig Naadam | **1,400 rating** (5.18: 1,800→1,600; 6.4: 1,600→1,400) | Ovoos **not stealable**, claim **interruptible by any hit**; rank rises toward centre; **B/A/S = 50/100/200**, paid at 5/10/20 per 3s over a **30s** window so late claims decay; KO **+8**, death **−8** (a 16-point swing over seen deaths) |
| Triumph | 1,400 rating | All Fields of Triumph required; 1 player per field, extra bodies don't help, **any enemy inside blocks capture**; snow ~16:00, auroras ~9:00 |

**Secure node rate per 3s:** 1→2, 2→4, 3→6, **4→10**, 5→12, 6→14, 7→18, 8→20, 9→22. Standing in a flag circle grants **Sheer Will** (+damage). Secure teleport pads go live **30s before** the weaponry spawn, grant 3s Invincibility, and **dismount you**. The centre pillar has fall-death punts — fight on the guardrailed ramps, not the pad edges.

**Triumph weather:** snow spawns blocking snow soldiers (the central gully crossroads is blocked — reroute early) and Blessed Blast AoEs that grant a **Snow Fort** barrier nullifying damage if you stand in them. **Auroras raise triumph ranks and fill everyone's Limit Break gauge** — hold LB for that window.

## Per-map playbook (compressed)

- **Secure** — hold 4+ nodes in a ring; collapse to the middle on the weaponry timer; nodes (+150) are the biggest single swing; never fight near the pad edges.
- **Seize** — be standing on the nearest tomelith for the **30-second opening spawn** (four activate together); win the fight at the tomelith, *then* channel; hold it to the end of the extraction or the value is wasted; a KO adds your data and subtracts theirs, so S-ranks are worth double.
- **Shatter** — Battle High converts directly into score; **watch the 30-second forecast icons and pre-position on the outline**, not on the fight; small ice at 12:30/4:30; large ice is back in 60 s, so taking a small ice is the more permanent gain; never attack another company's large ice from the middle field (it invites the pinch) and never drop off the cliffs on the right.
- **Danshig Naadam** — a race, not a defence: claimed ovoos cannot be stolen. Interrupt enemy claims with AoE. Decide as a team whether to commit to the central S-rank stalemate or farm A-ranks and stragglers while the other two bleed.
- **Triumph** — needs 3–4 small squads covering fields simultaneously; fields are blocked by any enemy inside, so harassment works; the central gully is ranged high ground; the death ball still wins it (community consensus).

## The 14 named plays

| # | Play | Source | One line |
|---|---|---|---|
| 1 | The 4× Rule | Lanchester | Count first: ≥1.5× engage fully, even = take the objective, fewer = disengage |
| 2 | The Defile | Lanchester linear law | Outnumbered? Fight where fire can't concentrate — corners, ramps, chokes |
| 3 | The Split Forcing | Lanchester inverted | Objectives are a dispersion machine; separating 24 into 12+12 halves their power |
| 4 | The Schwerpunkt | Clausewitz | One decisive point per phase, everything on it |
| 5 | The Floating Squad | Economy of force | 6–8 players never committed: plug flanks, exploit wins, counter-punch |
| 6 | The Pivot | Jomini, interior lines | Own the central position; reach every front first |
| 7 | Trade the Centre for the Ring | Liddell Hart | Cede the contested S-rank; take three mid-tier objectives at once |
| 8 | The Rear-Ring Raid | Liddell Hart | Hit the nodes they think are safe — then leave before respawns land |
| 9 | The Anvil and the Hammer | Sun Tzu cheng/ch'i | One third fixes, two thirds strike the exposed fraction |
| 10 | The Ghost Flank | Sun Tzu, deception | The enemy's only sensor is the map — eight riders can read as twenty |
| 11 | The Pre-Load | Boyd, OODA | Be on the objective before it spawns; use the public timers |
| 12 | The Sunk-Cost Strike | Boyd | Attack the moment they commit; force a choice between two losses |
| 13 | Break Contact on Victory | Clausewitz | Stop at the objective line — pursuit into 10s Invincibility respawns loses the match |
| 14 | The Quiet Leader | Coalition dynamics | As 1st: stay unclumped and out of the centre. As 3rd: create chaos |

Full derivations and citations: `references/military-doctrine.md`.

## Call sheet

| Element | Size | Mission |
|---|---|---|
| Command | 1 | declares objective and posture, nothing else |
| Scouts | 2, mounted | maintain sight-range contacts; treat empty map as unknown |
| Main body | 14–16 (tanks/melee) | the schwerpunkt; holds the pivot |
| Floating squad | 6–8 (burst melee + healer) | reserve: exploit, plug, counter-punch |

**Standing orders** (one clause, announced *before* needed): `REGROUP <place>` · `PUSH <objective> NOW` · `HOLD` · `BAIL` · `PINCH INCOMING <dir>` · `FLOAT` · `NO CHASE`.

**Rules of engagement:** 1) count first; 2) ≥1.5× → engage fully; 3) even → take the objective, don't fight; 4) fewer → bait, delay, disengage toward allies, find a defile; 5) won → stop, remount, take the objective, no pursuit; 6) losing → don't reinforce, redeploy.

## Doctrine audit — the ten named errors

Named violations correct pub behaviour better than generic advice: 8/8/8 split (Mass) · zerging off-objective (Objective) · no reserve (Security) · silence/six plans (Unity of Command) · marching into the contested centre (Manoeuvre) · chasing to the landing platform (Culminating point) · trickling back after a wipe (Economy of force — you are being defeated in detail) · job-swapping with Battle High (self-inflicted) · 1st place brawling in the open (invites a 2v1) · treating empty map squares as safe (Security).

## Posture by phase

- **0:00–4:00** — asymmetric and cautious; farm Battle High on stragglers; take the safe objective; never commit the reserve.
- **4:00–14:00** — mass + pivot; hold the interior position; contest the centre **only** as a 2-v-1 against the leader.
- **14:00–20:00** — if leading, quiet accumulation and no open melee; if behind, force the leader to split, no over-extension.

**The framing question that resolves mid-match arguments:** who is your enemy right now? 1st → the clock. 2nd → 1st's rate. 3rd → the stalemate.

## Callouts, macros and the call sheet

Three companion artifacts in the vault (`C:/ObsidianVaults/Notebook/Agents/ffxiv/guides/`):

- `ffxiv-frontline-macros.md` — 27 bilingual (EN/JP) callout macros with romaji, the sound-effect convention, hotbar layout, auto-translate appendix and a JP glossary.
- `ffxiv-frontline-call-sheet.md` — the one-page caller reference.
- `ffxiv-frontline-jobs.md` — the **full job/role workup**: what the five roles decide, the durability ladder, all fifteen role actions with the JP community's pick per job, the five-stage **kill chain**, counter-pairs, 21 job profiles, a 21×5 map-affinity matrix, and job-selection strategy. Load it for any "which job should I play / how do the roles interact" question.

**Client limits that silently break macros if ignored:**

- 15 lines per macro; **180 characters per line**; a blank line ends the macro.
- **Chat is throttled to roughly one message per second.** Two `/a` lines fired back-to-back lose the second one for readers — put both languages on a single line (`■ RETREAT / 撤退 <se.16>`) or insert `<wait.1>`.
- **Only one `/micon` is honoured per macro.** Placement convention differs: EN references say line 1; JP guides put it last in combat-action macros so the action fires first. For text callouts, line 1.
- `/a` = alliance chat = your entire 24-player Frontline team; enemies cannot see it.
- `/fmk D <me>` (`/fieldmarking`) drops **field marker D at your feet** — repeating it with `<wait.2>` creates a moving rally point ("follow me"), the JP commander standard. `/mk attack1 <t>` marks enemy targets; square marks the enemy commander by JP convention.
- `/mlock` stops another macro interrupting a multi-line sequence (use it on burst countdowns).
- `<se.1>`–`<se.16>` carry the message audibly — the JP community SE mapping is in the macro file.

**Bilingual strategy:** one line, `EN / JP`, `■` bullet prefix. Auto-translate dictionary phrases (定型文) render in the reader's own client language and are the only truly language-proof option, but they must be inserted with **Tab** in the macro editor — hand-typing them sends plain text that does not translate. So the literal bilingual line is the default and the dictionary is the supplement.

**JP vocabulary worth recognising:** 鳴らす (to fire a macro) · 軍師 (shot-caller) · リス (tomelith) · 大氷/小氷 (big/small ice) · 挟撃注意 (pincer) · 撤退 (retreat) · 深追い注意 (no over-pursuit) · 自陣OP (own base) · デジョン (Return) · 床ペロ (dying) · 凸る (charge in) · 芋る (play passively).

**Etiquette:** over-ringing alliance macros is the fastest way to be ignored — JP commanders explicitly warn against it. One call, one sound, then silence.

## Related skills

- `ffxiv-chat-translation` — JP↔EN callouts and macros for PvP parties.
