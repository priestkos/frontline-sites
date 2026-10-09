# Frontline Call Sheet — personal reference

One page. Read it in the 45-second prep window, then keep it on a second monitor.
Companion files: `ffxiv-frontline-complete-guide.md` (the full doctrine) and `ffxiv-frontline-macros.md` (the macro pack).

---

## 1. What you are

You are **the caller** — the single voice. If nobody else is calling, you are. A bad call that 20 people follow beats a good call that 5 follow.

| Element | Size | Who | Mission |
|---|---|---|---|
| **You (command)** | 1 | whoever will speak plainly | declare objective + posture. Nothing else. |
| **Scouts** | 2 | mounted mobility jobs | keep the map honest — the map only shows enemies *someone can see* |
| **Main body** | 14–16 | tanks + melee (they soak −40% to −55%) | the schwerpunkt: take the pivot, win the set-piece fight |
| **Floating squad** | 6–8 | burst melee + 1 healer | the reserve — **never** in the first wave |

**The reserve is the whole doctrine.** It plugs the third team's flank, converts a won fight into a captured objective, and counter-punches while the enemy is committed to your main body. A caller with a reserve beats an identical caller without one, every time.

---

## 2. The calls (with macro slots)

Fired on `/a` — the alliance channel. Full macro text in `ffxiv-frontline-macros.md`.

| Situation | Call | Macro | Key line |
|---|---|---|---|
| You need everyone in one place | RALLY / follow the D marker | M01 | `■ FOLLOW ME / 集合・追従` |
| Group is scattered | REGROUP | M02 | `■【REGROUP】/【集合】` |
| Pick the fight | CENTRE / EAST / WEST / NORTH / SOUTH | M03 / M04 | `卍 CENTRE 卍 / 中央` |
| Get ready to commit | BURST PREP (marker 1) | M08 | `【1タゲ付近】バースト準備` |
| Commit | COUNTDOWN 3-2-1 | M09 | `カウントダウン → 突撃` |
| Push now | PUSH | M10 | `【押し上げ】` |
| Lock a target | FOCUS THIS | M11 | `【これ集中・落とす】` |
| Third team closing on you | PINCER INCOMING | M14 | `【挟撃注意】` |
| Abort | RETREAT | M15 | `【撤退】` |
| Small step back | PULL BACK A BIT | M16 | `【少し下がって】` |
| Rebuild at the base | TO BASE - USE RETURN | M17 | `【自陣OPまで・デジョン】` |
| **The fight is won — stop** | **NO DEEP CHASE** | **M18** | `【深追い注意】` |
| You already have the score | PLAY SAFE | M19 | `【いのちだいじに】` |
| After a wipe | REGROUP — NO TRICKLE | M20 | `【立て直し・バラバラ禁止】` |
| You called something wrong | CORRECTION | M21 | `【訂正します】` |
| Objective focus | SECURE & DEFEND / ICE PRIORITY | M22 / M23 | `【大氷優先】` |
| Split the tasks | MAIN BODY / LIGHT PARTY | M24 | `本体は ／ ライトパーティは` |

**Press these three most: M01, M15, M18.**

---

## 3. Rules of engagement (count before you commit)

1. **Count first.** Their numbers on the map, yours on the minimap.
2. **≥1.5× their numbers → engage, fully and immediately.** Half-committing wastes the advantage (2:1 numbers = 4:1 killing power — Lanchester).
3. **Roughly even → don't fight, take the objective.** Walk past them. Let them come to *your* ground.
4. **Fewer than them → bait, delay, withdraw toward allies** (never toward your own base), and look for a **defile** — a corridor, corner or ramp where their numbers can't concentrate.
5. **Won the fight → stop. Remount. Take the objective.** No pursuit.
6. **Losing a fight → do not reinforce it.** Redeploy to something undefended. Reinforcing failure is how you get defeated in detail.

**Standing orders:** `REGROUP <place>` · `PUSH <objective> NOW` · `HOLD` · `BAIL` · `PINCH INCOMING <dir>` · `FLOAT` · `NO CHASE`.

---

## 4. Pre-match — the 45-second window

- [ ] Role action set in the PvP Profile (Tank: **Full Swing** on Secure, **Rampart** if focused; Melee: **Smite** for the reset-on-kill, **Swift** to escape; Healer: **Diabrosis** vs enemy healers, **Stoneskin II** if you're eating AoE).
- [ ] **Mount up.**
- [ ] **Map open and staying open.**
- [ ] Job decided. **Do not swap after you build Battle High — it resets to zero.**
- [ ] Note the Frontline Campaign Info timer for the first mid objective.
- [ ] Say one line in `/a`: "caller here, follow my calls, I'll ring for retreat" — people follow a named voice.

---

## 5. Phase script

### 0:00 – 4:00 — the approach
Cautious and asymmetric. **Do not commit the reserve.** Take the objective nobody is contesting, gang up on stragglers only, and build Battle High. Goal: be the team with Battle High when the first real fight happens.

### 4:00 – 14:00 — the main battle
Mass on the pivot. Contest the centre **only** as a 2-v-1 against whoever is leading — never as an even three-way brawl. Rotate on the timer, not on instinct.

### 14:00 – 20:00 — the decision
- **Leading?** Quiet accumulation. Hold what you have, avoid the open melee, stay unclumped. Your enemy is the clock.
- **Behind?** Force the leader to split. Threaten three objectives, take what they can't defend, and let the 2nd and 3rd bleed each other.

**Ask yourself at every pause: who is my enemy right now?** 1st → the clock. 2nd → 1st's rate. 3rd → the stalemate.

---

## 6. Map timings to call ahead of

| Map | Timer | Call |
|---|---|---|
| Secure | weaponry timer on the HUD; teleport pads live 30s before | "PADS IN 30 — MOUNT, PADS MID" — note the pads **dismount** you |
| Secure | node count | never drop below **4 nodes** (the 3→4 jump is 6 → 10 per tick) |
| Shatter | small ice at **12:30 and 4:30** remaining | be in position at :50 before it |
| Shatter | big ice ~30s in | "MID BIG ICE — BODY ONLY" |
| Triumph | snow ~**16:00** | reroute around the blocked gully crossroads *before* the fight |
| Triumph | auroras ~**9:00** | "LB INCOMING — HOLD IT FOR THE AURA" |
| Danshig | fewer, higher-rank ovoos late | "STOP CHASING S — TAKE THE A's" |

---

## 7. Secure — extra notes (the most mechanical map)

- **4 nodes is the floor.** 1→2, 2→4, 3→6, **4→10**, 5→12, 6→14, 7→18, 8→20, 9→22 per 3s.
- Mid values: **Nodes +150** · α drones +30 · Command Systems +24 · drones +10 · KO +10 · death −10.
- Standing in a flag circle grants **Sheer Will** (+damage) — so a defended flag is a bad fight for the attacker.
- **Fight on the guardrailed ramps, never near the pad edges.** The centre is a raised pillar; knockbacks (Full Swing, MCH/MNK/WAR toolkits) turn fights into fall-death KOs.
- The party with the most damage on a drone gets **Battle High for all its members** — worth a coordinated burn.

---

## 8. Live decision table (the doctrine plays as reflexes)

| You see this | Do this | Play |
|---|---|---|
| An 8-man enemy squad detached to a fringe node | Take the mass onto it — don't attack the 20-man blob | Anvil & Hammer |
| A fight they've already committed to | Hit them now; make them choose between the objective and the fight | Sunk-Cost Strike |
| They're clumped in the centre melee | Take three flanking objectives instead | Trade the Centre for the Ring |
| An objective near their base, unguarded | Raid it mounted — and **leave before their respawns land** (they exit with 10s Invincibility) | Rear-Ring Raid |
| Your main body is visible and the third team is watching | Hide the bulk, show two players, move the real push the other way | Ghost Flank |
| They've split to cover objectives you're threatening | Kill one half with everything | Split Forcing |
| You're outnumbered in an open field | Get to a corridor, corner or ramp — kill their number advantage | The Defile |
| You just won a fight | Take the objective, remount, **stop** | Break Contact on Victory |
| You're in 1st and a big brawl is forming | Stay out of it. Hold nodes. Announce your marker and stay unclumped | The Quiet Leader |

---

## 9. Do / Don't

**Do**
- Say the instruction, then stop talking. Silence is a command style.
- Announce a retreat **before** you need it.
- Correct a bad call immediately and loudly (M21).
- Name the objective, not the direction — "MID PILLAR", not "over there".
- Use `<se>` sounds so people react without reading.
- Praise one good action per match; cohesion is a moral force, and morale is what actually collapses in the last five minutes.

**Don't**
- Spam. Every `<se>` interrupts 23 people. Over-ringing is how callers get muted by the team.
- Run two plans at once.
- Let the reserve get sucked into the first fight.
- Chase to their landing platform.
- Feed a lost fight with reinforcements.
- Swap jobs mid-match after building Battle High.
- Emote at downed opponents — that's a **prohibited activity** and can be sanctioned.

---

## 10. Numbers on one line

**Rating:** Secure 2,400 · Seize 2,000 data · Shatter 1,600 data · **Onsal 1,400** · Triumph 1,400.
**Ovoo (Onsal):** B 50 / A 100 / S 200 · paid 5/10/20 per 3s over **30s** — value decays if the match ends mid-payout · KO +8, death −8 (16-point swing).
**Battle High:** max 100 · +10% damage & healing per 20 · BH V is announced match-wide · no loss on death (7.5) · **job change zeroes it**.
**Kill value:** 4/6/8/12/16/20 (KO) · 2/3/4/6/8/10 (assist), scaled by the victim's Battle High.
**Limit Break:** 1st place +25% slower charge · 3rd place +25% faster.
**Survivability:** tanks/melee −40% to −55% damage taken · ranged/casters only −25% to −35%.
**Objective:** 72 players · 24 per team · 20 minutes · premade max 4 · 10s Invincibility on leaving the base · any hit dismounts you (uncleansable Hoofing It).

---

*Written 2026-10-05, patch 7.5 era. Re-verify thresholds and job modifiers the patch after any major PvP balance change.*
