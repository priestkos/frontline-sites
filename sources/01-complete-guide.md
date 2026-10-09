# FFXIV Frontline — Complete Player Guide

**Win conditions · mechanics · per-map playbook · military doctrine · 14 named plays**

Reference patch: **7.5** (Dawntrail era). Frontline balance changes often — re-verify the numbers in Part 1/Part 2 after any major PvP patch.

Sources are listed in full at the end. Everything here is either a verified game mechanic (Lodestone patch notes, consolegameswiki) or explicitly labelled as doctrine/opinion.

---

## Table of contents

- [Part 0 — What Frontline is](#part-0--what-frontline-is)
- [Part 1 — Mechanics reference (the numbers that decide matches)](#part-1--mechanics-reference-the-numbers-that-decide-matches)
- [Part 2 — The five maps, in full](#part-2--the-five-maps-in-full)
- [Part 3 — The five levers that actually move win rate](#part-3--the-five-levers-that-actually-move-win-rate)
- [Part 4 — Per-map playbook](#part-4--per-map-playbook)
- [Part 5 — Jobs, role actions and compositions](#part-5--jobs-role-actions-and-compositions)
- [Part 6 — Pre-match checklist](#part-6--pre-match-checklist)
- [Part 7 — The doctrine: nine principles of war applied](#part-7--the-doctrine-nine-principles-of-war-applied)
- [Part 8 — Lanchester and the mathematics of the death ball](#part-8--lanchester-and-the-mathematics-of-the-death-ball)
- [Part 9 — Concentration, the reserve, and interior lines](#part-9--concentration-the-reserve-and-interior-lines)
- [Part 10 — The indirect approach: winning without the fight](#part-10--the-indirect-approach-winning-without-the-fight)
- [Part 11 — Time: the OODA loop and pre-loading](#part-11--time-the-ooda-loop-and-pre-loading)
- [Part 12 — The culminating point, and the pursuit that loses matches](#part-12--the-culminating-point-and-the-pursuit-that-loses-matches)
- [Part 13 — Coalition dynamics: how to play 1st, 2nd and 3rd](#part-13--coalition-dynamics-how-to-play-1st-2nd-and-3rd)
- [Part 14 — The 14 named plays](#part-14--the-14-named-plays)
- [Part 15 — The call sheet (command structure)](#part-15--the-call-sheet-command-structure)
- [Part 16 — The doctrinal error checklist](#part-16--the-doctrinal-error-checklist)
- [Part 17 — Posture by match phase](#part-17--posture-by-match-phase)
- [Part 18 — Quick reference card](#part-18--quick-reference-card)
- [Sources](#sources)

**Companion document:** [`ffxiv-frontline-jobs.md`](ffxiv-frontline-jobs.md) — the full job/role workup (five roles, all fifteen role actions, the kill chain, counter-pairs, 21 job profiles, per-map affinity matrix, selection strategy). Part 5 below is the short version.

---

## Part 0 — What Frontline is

Frontline is FFXIV's large-scale PvP mode, added in patch 2.3. Three teams of up to **24 players** fight under the banners of the three Grand Companies — **The Maelstrom**, **The Twin Adder** and **The Immortal Flames** — for a maximum of **72 combatants** on one map.

- **Match length:** 20 minutes maximum. Most matches are decided by rating, not by the timer running out.
- **Team assignment:** random. You cannot choose your Grand Company team.
- **Achievement credit:** PvP progress counts toward the Grand Company you are *pledged* to, not the one you're randomly assigned to.
- **Party size:** you may queue alone or as a premade of **up to four players**. This is the hard cap — you cannot bring a full 8-man party.

### Requirements and unlock

- Level 30+, Disciple of War or Magic.
- A **Soul Crystal** equipped (i.e. the first level-30 job quest for your class, or an expansion job unlocked on a base class).
- Enlisted in a Grand Company.
- Unlocked via the quest **"Like Civilized Men and Women"** from your Grand Company.
- **Mounts are not required but are effectively mandatory** — every Frontline map makes heavy use of mounts to cross large distances.

### The daily rotation

- The available campaign changes at **daily reset** (7:00 a.m. PST / 8:00 a.m. PDT).
- Only the currently available campaign can be reached through **Daily Challenge: Frontline** in the Duty Finder.
- The classic maps rotate in the order **Secure → Seize → Shatter → Danshig Naadam**, and since patch 7.4 **Worqor Chirteh (Triumph)** is paired alongside the rotating map (the 7.4 notes list the rotation as Seize/Triumph, Shatter/Triumph, Onsal/Triumph, Secure/Triumph).

### Rewards

| Reward | 1st | 2nd | 3rd | Condition |
|---|---|---|---|---|
| PvP EXP | 1000 | 750 | 500 | — |
| Series EXP | 1500 | 1250 | 1000 | — |
| Wolf Marks | 1000 | 750 | 500 | — |
| PvE EXP | 12% of a level | 11% | 10% | Below level cap |
| Allagan Tomestones of Poetics | 50 | 50 | 50 | Above level 50 |
| Allagan Tomestones of Mathematics | 50 | 50 | 50 | Level-capped |
| Allagan Tomestones of Mnemonics | 20 | 20 | 20 | Level-capped |

- Tomestones are only awarded to players **level 50 or higher**.
- **Consolation mechanic:** if your team ranked 3rd, PvP EXP, Series EXP and Wolf Marks are increased by **10% for each consecutive 3rd-place finish, up to +50%**. The bonus carries over if you then place 2nd, and resets entirely on a 1st-place finish.

### The landing platform

- Each Grand Company has a **landing platform** — a safe zone where jobs may be changed freely and PvP Role Actions set, and where you are revived after being KO'd.
- Each team gets **45 seconds** confined to their platform at the start for preparation.
- Players who leave the landing platform receive a **10-second Invincibility** buff, which exists specifically to prevent spawn camping.
- You can return to your platform at any time with **Return**, which is how you change jobs mid-match (**this resets your Battle High to zero**).

### Mounts

- Mounts are freely usable. Flying and pillion riding are disabled.
- **Any incoming attack forcibly dismounts you** and applies the **Hoofing It** debuff. This debuff must be waited out — it **cannot be cleansed with Purify**.
- Practical consequence: mount for rotation, **dismount voluntarily before contact**.

### Communication and conduct

- Chat is unrestricted and enemies cannot see it. Use it. Emotes are unrestricted.
- Excessively emoting at downed opponents is a **Prohibited Activity** that may result in account sanctions.
- Performance Actions are disabled.

### The map

- All objective states are marked on the standard map.
- The map shows **all friendly players**, and shows **enemy players only if they are within sight range of any friendly player** (as coloured triangles).
- This is the single most important information asymmetry in the mode, and Part 10 exploits it deliberately.

---

## Part 1 — Mechanics reference (the numbers that decide matches)

### KDA — Knockout, Defeat, Assist

If you land the finishing blow (Knockout) or contribute to it (Assist) you gain Battle High rating. The amount depends on **the defeated player's own Battle High rating**:

| Defeated player's Battle High | Rating from Knockouts | Rating from Assists |
|---|---|---|
| No Battle High | 4 | 2 |
| Battle High I | 6 | 3 |
| Battle High II | 8 | 4 |
| Battle High III | 12 | 6 |
| Battle High IV | 16 | 8 |
| Battle High V | 20 | 10 |

**Being knocked out loses your team points**, and awards points to the team that killed you. In Secure this is an explicit **−10 / +10**; in Shatter a KO is worth **+8 data** to the killer's team.

### Battle High

Battle High is a status that increases **damage dealt and HP restored by healing actions** (including barriers such as Burst).

| Status | Rating | Effect |
|---|---|---|
| Battle High I | 20–39 | Damage dealt and healing potency +10% |
| Battle High II | 40–59 | +20% |
| Battle High III | 60–79 | +30% |
| Battle High IV | 80–99 | +40% |
| Battle High V | 100 | +50% |

- Maximum rating is **100**; every increment of 20 raises the tier.
- A player reaching **Battle High V is announced to the entire match**. Expect to be focused.
- **As of patch 7.5, being incapacitated no longer reduces your Battle High rating.** (Historically a death halved it.) The cost of dying is now tempo and rating, not your power curve.
- **Changing jobs completely resets the Battle High gauge.** This is the most common self-inflicted loss of a match in progress.
- In Secure, Battle High is also earned by fulfilling objectives (notably defeating the mid-map Allagan machinery).

### Limit Break charge times

To promote balanced matches, Limit Break charge time varies with your Grand Company's current standing:

- **1st place: 25% slower** charge time
- **2nd place: normal**
- **3rd place: 25% faster** charge time

This is a deliberate rubber band. If you are behind, the game has handed you a tool — spend it on the leader.

### Job modifiers

Damage dealt, damage taken and Limit Break charge time all vary by job. This table is what determines who can physically stand in a fight.

| Job | Damage dealt | Damage taken | LB charge time |
|---|---|---|---|
| Paladin | — | −45% | +15s |
| Warrior | −10% | −50% | — |
| Dark Knight | −15% | −40% | +45s |
| Gunbreaker | — | −55% | +15s |
| Monk | — | −55% | — |
| Dragoon | −10% | −50% | +15s |
| Ninja | — | −45% | +15s |
| Samurai | −5% | −55% | +15s |
| Reaper | — | −50% | +15s |
| Viper | −5% | −55% | — |
| Bard | — | −30% | −15s |
| Machinist | — | −30% | — |
| Dancer | — | −35% | +30s |
| Black Mage | −5% | −30% | — |
| Summoner | −10% | −30% | +15s |
| Red Mage | — | −45% | — |
| Pictomancer | −10% | −30% | — |
| White Mage | −10% | −25% | +15s |
| Scholar | −10% | −30% | — |
| Astrologian | −15% | −25% | +15s |
| Sage | — | −35% | — |

**Read this table as a survival ranking.** Tanks and melee soak **−40% to −55%** damage. Ranged and casters take only **−25% to −35%**. A Black Mage, White Mage or Astrologian caught in the open is a free kill; a Warrior, Gunbreaker, Monk or Samurai is not.

### Role Actions (PvP) — added in patch 7.2

Available only in **Frontline, Rival Wings and the Wolves' Den Pier**. Each of the five roles (tank, healer, melee DPS, physical ranged DPS, magical ranged DPS) has **three actions, of which you may select one**. You set it in **PvP Profile** under Character in the main menu, outside large-scale PvP, or while in the starting area inside a large-scale PvP duty.

**Tank**

| Action | Recast | Effect |
|---|---|---|
| Rampage | 45s | 8,000 potency to all nearby enemies; target's damage taken **+25%** for 10s |
| Rampart | 60s | Damage taken **−50%**, HP recovered by healing **+25%** for 15s |
| Full Swing | 30s | 8,000 potency, **30-yalm knockback**, removes Guard from enemies under its effect |

**Melee DPS**

| Action | Recast | Effect |
|---|---|---|
| Bloodbath | 45s | Damage dealt +10%, converts 100% of damage dealt into HP, 10s |
| Swift | 30s | Movement speed **+100%**, immunity to Stun, Heavy, Bind, Silence, Half-asleep, Sleep, Deep Freeze, and knockback/draw-in effects, 4s. Ends on mounting. |
| Smite | 15s | 6,000 potency, rising to **18,000** as target HP falls (max at ≤25% HP). **Recast resets on a kill or assist.** |

**Healer**

| Action | Recast | Effect |
|---|---|---|
| Haelan | 2.4s | Restores target HP, cure potency 15,000 |
| Stoneskin II | 30s | Barrier on self and nearby party members absorbing damage equal to a 12,000-potency heal, 10s |
| Diabrosis | 45s | 9,000 potency unaspected damage to target and nearby enemies; target's **HP recovered by healing −33%** for 10s |

*The physical ranged and magical ranged role-action sets are not enumerated in the sources used here; the physical ranged set includes **Dervish** (damage near the point of impact). Check your PvP Profile for the current lists.*

### Frontline Campaign Info

A HUD element added in patch 7.2 showing the time to the next objective spawn (and, on Worqor Chirteh, capture progress and weather changes). **Watch it constantly** — it is the difference between arriving at an objective and reacting to it.

---

## Part 2 — The five maps, in full

### 2.1 The Borderland Ruins (Secure) — Carteneau Flats

*Added patch 2.3. Removed in 6.4 for revision; returned in patch 7.2 significantly reworked.*

**Victory:** reach **2,400 tactical rating**, or hold the highest rating when time expires. Simultaneous 2,400 = draw.

Rating changes as of patch 7.25:

| Action | Rating change |
|---|---|
| Defeat Interceptor Drones | +10 |
| Defeat Interceptor Drones α | +30 |
| Defeat Interceptor Command Systems | +24 |
| Defeat Interceptor Nodes | **+150** |
| Knock out an opposing player | **+10** |
| Be knocked out | **−10** |

**Key locations.** Nine occupiable locations (outposts and Allagan ruins) marked by flags, all unoccupied at the start. Standing in proximity to a flag captures it; capture speed scales with the **number of your players** in proximity. An enemy coming within proximity of your flag turns it neutral. There is a capture jingle and a "Torn from the Heavens" motif when you lose one.

Standing inside the flag circle grants **Sheer Will**, a large damage-dealt buff — so attacking a defended flag is a bad fight for the attacker.

Sustained rating per three seconds:

| Key locations held | Rating gained per 3s |
|---|---|
| 1 | 2 |
| 2 | 4 |
| 3 | 6 |
| **4** | **10** |
| 5 | 12 |
| 6 | 14 |
| 7 | 18 |
| 8 | 20 |
| 9 | 22 |

**The breakpoint is 4.** Going from 3 to 4 nodes jumps your rate from 6 to 10 per tick. Four nodes is the floor; more is better but the curve is flattest between 5 and 7.

Teams usually capture in a clockwise or counter-clockwise ring. The location directly in front of each Grand Company's base is tilted in favour of its defender, and many teams simply stop their advance there.

**The middle: Allagan weaponry.** Periodically the weaponry displacement system spawns Allagan machinery in the centre. The time to the next deployment is on the Frontline Campaign Info HUD.

- **30 seconds before a spawn**, one-way personnel displacement panels on three sides of the map activate. Entering one teleports you rapidly to the centre **with a 3-second Invincibility buff**, but **dismounts you**.
- The centre is a raised pillar a considerable distance above the ground. **Many jobs (tanks with Full Swing in particular) will punt players off the ledges, which usually means an instant KO from fall damage.** The areas around the ramps are safest (guardrails); the areas around the teleporters are the most dangerous.
- **Interceptor Drones** spawn on the six outer hexagonal tiles, use **Auto Cannon** (a line AoE with roughly a 30-yalm knockback), and continuously respawn while the system is active. The party contributing the most damage gains the rating, Battle High and Prime Air achievement credit. **Gold drones award more rating and Battle High.**
- **Interceptor Command Systems** deploy as a new enemy (patch 7.2) using **Perimeter Cannon**; absorbing this attack increases your rating and gains tactical points for your team.
- **Interceptor Nodes** are worth **+150** — by far the largest single objective swing on the map.

Other patch 7.2/7.25 notes: terrain adjusted, key location distribution adjusted, rating per node count adjusted, Sheer Will added, enemy spawn patterns and drone/node actions adjusted, and the team contributing most damage to a drone now grants **Battle High rating for all its members**.

### 2.2 Seal Rock (Seize)

*Added patch 3.05 (Heavensward).*

**Victory:** accumulate the required amount of **Data** — **700** in the 72-player campaign, following the patch 6.4 **reduction** from 800 (the wiki no longer publishes a figure, so confirm on the HUD) — or hold the most Data at expiry. Rewards are ranked by Data collected.

**Data comes from two sources:** occupying Allagan Tomeliths, and defeating enemy players (which both adds to your total and subtracts from theirs).

**Allagan Tomeliths — when they activate.**
- All are **inactive at the start**. The map holds roughly **16 tomeliths** and they activate at set intervals.
- **The opening is scripted: four tomeliths activate 30 seconds after the match begins.** After that, activation follows *extraction*, not the clock.
- **Spawn points are fixed; the order is random.**
- Each holds a limited quantity of data and **deactivates when it is drained**. It pays for as long as it holds data, so somebody has to stay on it.
- **A drained tomelith is replaced about 15 seconds later** by another one activating somewhere else. Watch the map, not the spot you were standing on.
- **Full extraction takes about two minutes**, and the total is fixed by rank:

  | Rank | Rate while occupied | Total, held from activation to empty |
  |---|---|---|
  | **B** (triangle) | 2 data per 3 s | **80** |
  | **A** (square) | 3 data per 3 s | **120** |
  | **S** (pentagon) | 4 data per 3 s | **160** |

  A rank is therefore a **duration** as much as a value: a B is only worth taking if you can hold it for most of two minutes.
- **The map thins out and gets richer.** The maximum number active at once changes over the campaign: it opens at **four**, and as the match runs the number that spawn **decreases** while the rank that spawns **rises**. Expect a wide, cheap, B-heavy opening and a narrow, expensive, A-and-S endgame.
- Tomeliths activate at one of three ranks — **B, A, S** — higher ranks are rarer but hold more data. As the match progresses, higher ranks become more likely.
- **They can be stolen.** Occupying is a long channel that is **interrupted by any hit**, and an enemy team can claim it after your team has activated it. The ongoing ticks are what pay, so steal back for the denial rather than for any bonus on the claim itself.

The team's Data total is shown on the dedicated scoring banner.

### 2.3 The Fields of Glory (Shatter)

*Added patch 3.3 (Heavensward).*

**Victory:** collect **1,600 Data**, or hold the most at expiry. Simultaneous 1,600 = draw. *(Raised 1,600 → 2,000 in patch 6.4, then lowered back to 1,600 in patch 6.57.)*

**Data comes from two sources:**
- **Destroying Icebound Tomeliths:** **+1 to ~200** depending on the size of the tomelith and the damage you inflicted. Rewards cap at **50 for a small tomelith** and **200 for a large tomelith**.
- **Defeating enemy players: +8 data.**

**Icebound Tomeliths ("ice") — when they activate.**
- Small ice has **300,000 HP**; large ice has **3,000,000 HP**. Data: small caps at **50**, large at **200**.
- **Ice is only damageable while active.** Every tomelith on the map is inactive at the start, and the order in which they activate differs every match.
- **You always get 30 seconds of warning.** An activation-forecast icon appears on the 2D map **30 seconds before** an ice becomes active, and the tomelith lights up where it stands. That warning is the whole map: it is how you arrive before the other two companies instead of after them.
- **The four map states, in order.** Read these off the map and you always know what is about to happen:

  | State | What you see | Meaning |
  |---|---|---|
  | **Gone** | not on the map | destroyed, awaiting respawn |
  | **Black** | on the map, dark | respawned but **not yet damageable** |
  | **Outlined** | outlined icon | the **30-second warning**; about to activate |
  | **Blue** | lit | **active and damageable** |
- **The opening.** The first forecast shows as the match starts and the first ice becomes damageable roughly **15 to 30 seconds in**, with **two large ice** activating together. In general there are always **two large ice primed to activate** and a maximum of **two large ice active at once**.
- **Small ice activates in waves.** The two wave times you can plan around are **12:30 and 4:30 remaining** on the timer. These are community-observed rather than an official figure, and they do not reconcile exactly with the official timers below, so trust the map outline over the clock.
- **The official timers (patch 6.55, unchanged since):**

  | Thing | Value |
  |---|---|
  | Time before the **first small ice** activates | **420 seconds** (7 minutes) |
  | Time for **small ice to reactivate** | **420 seconds** |
  | Time for destroyed **small ice to reappear** | **360 seconds** (6 minutes) |
  | Time for destroyed **large ice to respawn** | **60 seconds** |
  | **Small ice active at once** (maximum) | **15** |
  | **Large ice active at once** (maximum) | **2** |
- **Large ice comes back in a minute; small ice does not.** Large ice respawns in **60 seconds**, so the contest over it never really ends. Small ice is gone for **six minutes**, so a small ice your company takes is one the others cannot answer for a long time. That asymmetry should decide late target choice.
- **By the end of the campaign every tomelith on the map will have activated at least once.**
- **Battle High is critical here.** Faster kills of ice = faster score. A successful Grand Company places equal or greater importance on Battle High than on anything else.

**Positioning and plays.**
- Three of the four large ice are connected via a **ramp to the left of a Grand Company's landing platform**. Attacking another company's large ice is extremely risky. Attacking from the middle field in particular **invites a flank ("pinch") by the third Grand Company.**
- Dropping down from the cliffs to the right of the landing platforms **cuts off your own retreat** — a committal play usually best avoided.
- The **middle large ice** is the scene of the most intense fighting, since it is freely accessible to all three companies.

### 2.4 Onsal Hakair (Danshig Naadam)

*Added patch 5.15 (Shadowbringers).*

**Victory:** reach **1,400 tactical rating**, or hold the highest at expiry. *(Lowered 1,800 → 1,600 in patch 5.18, then 1,600 → 1,400 in patch 6.4.)* Rating comes from claiming **ovoos** and defeating enemy players (which raises yours *and* lowers theirs).

**Ovoos** are sacred sites with four states:

1. **Inactive** — cannot be claimed, but you should note the position for when it activates.
2. **Activating** — a symbol appears above it showing its rank and time to activation; the symbol gradually completes.
3. **Active** — claimable by interacting. **If you are attacked while claiming, the process is interrupted.**
4. **Claimed** — it increases that team's rating over time.

**Critical difference from Seize: a claimed ovoo cannot be seized by the opposition.** Once claimed, the points are yours for its duration. After a time it simply returns to inactive.

**Rank — and what a claim actually pays.** When an ovoo activates it is randomly assigned **B, A or S**, shown by its shape:

| Rank | Shape | Total payout | Rate | Payout window |
|---|---|---|---|---|
| **B** | blue triangle | **50** rating | +5 per 3s | 30 seconds |
| **A** | red diamond | **100** rating | +10 per 3s | 30 seconds |
| **S** | yellow pentagon | **200** rating | +20 per 3s | 30 seconds |

An ovoo **pays out continuously for 30 seconds** after the claim, then vanishes and a new ovoo appears immediately. Therefore **a claim is worth `rate × seconds left in the match`, capped at its rank total**. A tick lands every 3 seconds, so a partial final window still pays:

| An S ovoo claimed with… | You actually bank |
|---|---|
| 30s left | 200 |
| 20s left | 120 |
| 15s left | 100 |
| 10s left | 60 |
| 6s left | 40 |

In a 1,400-point match a full S claim is **14% of the win** in one action; a B claim is 3.6%. If your alliance sits at 1,350 and an S ovoo is up with 20 seconds left, that claim **ends the match**.

Higher ranks are rarer and **the closer to the centre of the battlefield, the greater the likelihood of a high rank.** As the battle progresses the number of simultaneously active ovoos **decreases** while the likelihood of high ranks **increases** — the late game is typically **one or two S-rank ovoos** and few A-ranks. Late-game ovoo value is *concentrated*, not reduced: this is the one map where the endgame is more about objectives than the midgame is.

**Kills on this map.** A KO is **+8** and being KO'd is **−8**, flat — *not* scaled by the victim's Battle High (Battle High scales only your own damage and healing). A death is therefore a **16-point swing**: about a third of a B-rank ovoo, 8% of an S. You cannot win this map by farming kills; you can lose it by feeding them.

The centre S-rank ovoo is intended to be contested by all three teams and frequently becomes a long stalemate.

**Community doctrine for the endgame.**
- Claims, not kills, decide the map. **Claim any ovoo you can complete unchallenged**, because a claimed ovoo cannot be taken back — with 30 seconds left that is uncontestable insurance.
- **Denial is cheap.** Breaking an enemy claim costs one ranged hit from outside the circle. While leading, shadow the ovoo the trailing team needs rather than fighting their main body.
- **Do not garrison a claimed ovoo.** Claim it and leave; the points are already yours.
- **One claimer, the rest screening.** Because any damage interrupts the claim, put one player on the ovoo and everyone else in a ring facing outward.
- The map's phases are legible from what is spawning: **early** = many B, occasional A · **mid** = two or three A at once, rare S · **late** = one or two S, rare A. Chase rank as the match matures.
- **Pincer the highest-scoring alliance.** Handing space — even points — to the lowest-ranked alliance is often correct: you win when someone else collapses, and the leader is the only team that can beat you.
- If you are **3rd**, never fight the team just above you. You need them to overtake the leader.

**Claim or fight? — the endgame decision matrix.**

| Your position | Claim? | Fight? |
|---|---|---|
| **Within ~one ovoo of 1,400** | Yes — anything, immediately. Crossing 1,400 ends the match instantly and cannot be answered. | No. Avoid contact entirely. |
| **Ahead, far from the threshold, 2nd far behind** | Yes — uncontested ovoos on your path, nothing more. | **No.** The clock is your ally; deaths are your only enemy. Deny their claims, don't brawl. |
| **Ahead, but 2nd is near the threshold** | Yes — it is now a **race**: your claim rate against theirs. | Yes, but only to **interrupt their claims** — one ranged hit from outside the circle breaks a channel. The cheapest denial in the mode. |
| **3rd** | Yes — the cheap B ovoos both leaders are ignoring. | **Never** the team just above you; you need them to overtake the leader. Pincer the leader instead. |
| **Two others are fighting** | Yes — hoover ovoos while they bleed, then hit the exhausted winner. | Only the winner, and only with numbers. |

**The rate race.** Because everything in Frontline pays per 3 seconds, breadth beats quality: **six B ovoos held = 30 rating/3s; one S held = 20 rating/3s.** Take the cheap ovoos nobody wants, not only the shiny one.

### 2.5 Worqor Chirteh (Triumph)

*Added patch 7.4 (Dawntrail).*

**Victory:** reach **1,400 tactical rating**, or hold the highest at expiry.

**Triumphs** have four states: **Inactive → Activating → Unclaimed → Claimed.**

**Fields of Triumph.** When a triumph is **unclaimed**, several fields appear around it. **Once a single team secures all fields, that team claims the triumph.**
- The **number of fields equals the vertices of the triumph shape** — a triangle has three fields, a diamond has four.
- **Only one player is required to stand in each field** to capture it. **More players do not speed it up.** Once a field is captured, the player may leave it and move to another.
- **Fields cannot be captured while a member of an opposing Grand Company is inside the contested area.**
- Capture progress is shown in the **Frontline Campaign Info** HUD element.
- A **claimed** triumph increases rating over time and **cannot be seized** by the opposition; after a while it reverts to inactive and a triumph **elsewhere** becomes unclaimed.

**Rank.** On activation a triumph is randomly assigned **B, A or S**, indicated by its shape. Higher ranks are rarer but generate rating faster. Higher rank = **more fields to capture**.

**Terrain.** Triumphs in the **central gully** are harder to capture, because ranged jobs can attack from above.

**Weather.** Two weather events, on a fixed schedule:

- **Snow — approximately 16:00 remaining.** Snow spirits appear and cast **"Soldiers of 'Fridgeration"**, creating snow troops of various sizes around the arena as **obstacles**. The triple crossroads in the central gully is blocked by a large snow soldier, **forcing the long way around**. The spirits also repeatedly cast **Blessed Blast** — icy circle AoEs, slowly filled in — and players caught in the blast are protected by a **Snow Fort** barrier that **nullifies damage** (a usable absorb/bait tool).
- **Auroras — approximately 9:00 remaining.** Two effects: **increases the likelihood that triumphs activate at a higher rank**, and **gradually fills the limit gauge of all players**.

Claimed triumphs and weather changes are announced in the battle log.

---

## Part 3 — The five levers that actually move win rate

1. **Someone has to call the shots.** Every credible guide says the same thing: a shot-caller with macro'd calls beats raw job quality. If nobody is leading, lead — even badly. This is the highest-return action available to an individual player.
2. **Fight as one mass.** A 20-player body beats three roving six-man groups every time: it wins the fight, farms Battle High from it, and then takes the objective with the damage buff. Scattered players feed Battle High to whoever is grouped.
3. **Farm Battle High early, then protect your position.** You want Battle High before the first big objective. Take safe fights only — gang up on stragglers, never 1v2, never dive a guarded group. Once you are BH IV–V you are announced to the whole match: stay **inside** your body, not on its edge.
4. **Play the leader, not the scoreboard.** As 2nd or 3rd, your target is the 1st-place team: deny their objectives, pinch them while they are engaged with the other team, and never let them farm free kills off the weakest team.
5. **Minimap up at all times, rotate on mounts.** Objectives and enemy triangles exist only on the map. Fringe objectives nobody is defending are free points; the middle is where you go with your team only.

**Discipline rule that saves runs:** start overly cautious. Disengage at roughly half MP, retreat **toward your team** (never toward your spawn), and treat not dying as worth more than chasing a kill — deaths hand the enemy both rating and Battle High.

---

## Part 4 — Per-map playbook

### Secure — the node ring
- **Treat four nodes as your floor.** The 3→4 breakpoint doubles your income rate (6 → 10 per tick).
- Rotate the ring clockwise, and **collapse to the middle when the weaponry timer is close**. Be on the pad 30 seconds early; the teleport dismounts you, so mount up again before you land in a fight.
- Mid objectives in value order: **Nodes (+150) > gold/α drones (+30) > Command Systems (+24) > drones (+10)**.
- **Fight on the ramps with guardrails, not near the teleport pad edges** — the centre is a raised pillar and knockbacks (Full Swing, MCH/MNK/WAR toolkits) turn fights into fall-death KOs.
- Take the node off the enemy, then kill the enemy — the party with the most damage on a drone gets Battle High for **all its members**.

### Seize — hold and contest
- Tomeliths are **stealable** and the channel is interrupted by any damage. The correct sequence is always: **win the fight at the tomelith, then channel.**
- A KO both adds your Data and subtracts theirs — fights at S-rank tomeliths are worth double.
- Stay mobile. Flank the leader. If you are leading, secure the tomeliths on your own side of the map and watch the 2nd-place team specifically.

### Shatter — damage race
- Only **damage dealt to ice** pays. Small ice caps at 50 data, large at 200; small ice is 300k HP, large is 3M HP.
- **Battle High literally converts into score here**, because 50% more damage means faster breaks.
- **Small ice always spawns at 12:30 and 4:30 remaining.** Be in position beforehand.
- Never attack another company's large ice from the middle field — that lane invites the third team's pinch. Never drop off the cliffs to the right of a landing platform; it commits you with no retreat.
- The centre large ice is the set-piece fight. Win it or deny it; do not lose 8 players trying to solo it.

### Danshig Naadam — first to the ovoo wins it
- Claimed ovoos **cannot be stolen**, so this is a pure race: be there before it activates.
- **Interrupt enemy claims with AoE** — any hit breaks the channel, and one AoE can interrupt several players at once.
- Rank rises toward the centre (B → A → S), and late game means fewer but richer ovoos.
- The centre S ovoo is a deliberate three-way stalemate. Decide as a team whether to commit or to farm contested A-ranks and stragglers while the other two bleed each other.
- If you are 1st, sit on the ovoo side of the map. If you are 2nd or 3rd, deny the leader and let them fight the third team.
- Roving players who ignore the central stalemate can quietly take objectives and win under everyone's nose.

### Triumph — spread thin, then concentrate
- A triumph needs **all its fields** captured, each field needing **one** player and being **blocked by any enemy inside it**. So this map rewards **three or four small squads covering fields simultaneously** and punishes 3v15 fights at safe nodes.
- The central gully is a ranged job's dream (attack down from the rim) and the hard way to capture from below.
- **Snow (~16:00):** reroute early — the triple crossroads is blocked by a large snow soldier. Use the Blessed Blast indicators deliberately: standing in one gives you a **Snow Fort** shield that nullifies damage.
- **Auroras (~9:00):** higher-rank triumphs become likely **and** everyone's Limit Break gauge fills. Hold your LB for this window.
- Community consensus (r/ffxiv): the death ball still wins this map. A team that only farms uncontested nodes will lose the moment either other team starts contesting objectives.

---

## Part 5 — Jobs, role actions and compositions

> **Full treatment in the companion document [`ffxiv-frontline-jobs.md`](ffxiv-frontline-jobs.md)** — the five roles, all fifteen role actions with the JP community's pick per job, the five-stage kill chain, counter-pairs, 21 job workups, a 21×5 map-affinity matrix, and selection strategy. The below is the short version.

### Where the meta sits

From role modifiers plus community reporting:

- **Warrior** — denies Guard with minimal risk, survives everything, useful even at low skill.
- **Ninja** — absorbs substantial damage, deals significant damage even when played badly, hard to kill when played well. Strong solo pick.
- **Bard** — constant group-wide Limit Break gauge support; one of the few jobs whose value rises dramatically with experience.
- **Gunbreaker** — good durability and tide-turning burst, but precision-dependent.
- **Reaper** — commonly cited top solo pick.
- **Dark Knight** — solid, but carries a stigma from its over-tuned past; many players never learned to play it properly and dive in and die.
- **Viper** — strong but complex; rarely played well in random matches.
- **Machinist** — punts players off ledges on Secure; situational elsewhere.

**The honest summary:** job fit beats tier lists. Role modifiers mean tanky jobs are the ones who can stand on an objective while it ticks. A coordinated WAR + healer + two melee quartet out-wins an uncoordinated team of higher-tier picks.

### Compositions

You can only queue with **three other players**, so build the standard four-piece:

- **Tank** — the vanguard. Front of the formation, always the initiator. The party does not engage until the tank engages.
- **Healer** — rear of the formation, out of enemy range but within healing range. Priority one is the tank; top up DPS if the situation allows. If the tank dies, the group usually follows.
- **Two DPS** — several steps behind the tank, out of harm's way but close enough to burst a target the moment the tank commits.

**Voice chat is a large advantage** but macros can substitute. The key is that everyone follows the caller in a split second.

### Role-action picks that matter

- **Tank → Full Swing** on Secure (the ledge punt), **Rampart** if you are being focused, **Rampage** when the enemy healer is the target.
- **Melee → Smite** for the reset-on-kill snowball, **Swift** to escape a collapsing fight, **Bloodbath** for extended solo duels.
- **Healer → Diabrosis** is the anti-healer button (−33% healing received); **Stoneskin II** if your group is eating AoE.
- **Physical ranged → Bravery** almost always: **+25% damage dealt *and* −25% damage taken** for 15s on a **30s** recast — the strongest role action in the mode.
- **Magical ranged → Phantom Dart** (+25% damage taken on the target, 15s recast); **Comet** (20,000 potency) only when you can stand still for the 2.4s uncancellable cast.

---

## Part 6 — Pre-match checklist

1. Set your **role action** and hotbars in the PvP Profile **before** queueing.
2. Open the map the second you load, and **leave it open**.
3. Decide your job before the gate. You may swap at the base, but **swapping resets Battle High** — decide once and commit.
4. Read the **Frontline Campaign Info** timer: it tells you before Secure weaponry and other mid objectives go live.
5. **Mount before the gate opens.**
6. First fights: pick stragglers only, build Battle High, then commit.
7. Nominate or become the caller. One voice.

---

## Part 7 — The doctrine: nine principles of war applied

Military doctrine compresses strategy into nine principles, conventionally memorised as **MOOSEMUSS**: **M**ass, **O**bjective, **O**ffensive, **S**ecurity, **E**conomy of force, **M**anoeuvre, **U**nity of command, **S**urprise, **S**implicity.

Run a Frontline match through them and the failures are legible at a glance.

| Principle (doctrinal wording) | Frontline translation | The failure it names |
|---|---|---|
| **Objective** — direct every operation toward a clearly defined, decisive, attainable objective | The win condition is a **rating threshold**, not kills | Farming kills off the objective |
| **Offensive** — seize, retain and exploit the initiative | Whoever decides *where the next fight happens* wins | Reacting to enemy triangles all match |
| **Mass** — concentrate combat power at the decisive place and time | One 20-man body, not three 8s | The 8/8/8 split (the default pub failure) |
| **Economy of Force** — allocate minimum essential power to secondary efforts | Two scouts, one reserve — not half your team | Sending 12 players to a fringe node |
| **Manoeuvre** — place the enemy at a disadvantage by flexible application of combat power | Terrain plus arrival timing | Taking the fight they chose |
| **Unity of Command** — unity of effort under one responsible commander | **One caller** | Six people typing six plans |
| **Security** — never permit the enemy an unexpected advantage | Reserve plus flank watch | Getting pinched by the third team |
| **Surprise** — strike at a time, place or manner for which he is unprepared | Rear-ring nodes, off-timer pushes | Marching into the contested centre |
| **Simplicity** — clear, uncomplicated plans and concise orders | "REGROUP SOUTH." One clause. | The three-part plan nobody reads |

Doctrinal note: the nine principles are linked through the **master principle — the objective**. Everything else exists to serve it.

---

## Part 8 — Lanchester and the mathematics of the death ball

**Lanchester's square law:** when forces engage with aimed fire at range — where each unit can shoot at any target and receive fire from any direction — **combat power is proportional not to the number of units but to the square of the number of units.**

Worked examples from the literature:

- 2 vs 3 units → the advantage is 3² − 2² = **5**
- 2 vs 4 units → 4² − 2² = **12**
- 2 vs 5 units → 5² − 2² = **21**
- A 2:1 numerical advantage yields **4×** the firepower and inflicts four times the punishment.
- A 3:1 numerical advantage is a **9:1** combat-power advantage.
- Also: **group fighting ability rises with the square of group size but only linearly with individual fighting ability.** Defeating an adversary three times as numerous would require fighters **nine times** as effective.

Frontline is square-law warfare: AoE damage means every player can hit every target in a blob. Three derived rules:

### The 4× Rule
Before any engagement, count.
- **≥1.5× their numbers → engage, fully and immediately.** Half-committing throws away the advantage you paid for.
- **Roughly even → do not take the fight. Take the objective.** Walk past them.
- **Outnumbered → do not engage at all.** Bait, delay, withdraw toward allies.

### The Defile (converting the square law to a linear law)
The square law holds only where fire can be concentrated. Lanchester's own conclusion: *concentrated fire favours a square-law outcome, whereas positional fire and one-to-one combat favour a linear-law outcome.*

So **when outnumbered, fight where fire cannot concentrate**: corridors, corners, stairs, narrow ramps, line-of-sight-breaking terrain. This converts the enemy's n² into n¹, and it is the only doctrinally sound way a smaller group beats a larger one in Frontline. It is also why chasing a routed enemy into a bottleneck is a gift to *them*.

### Split Forcing (inverting the law onto the enemy)
You do not have to kill their 24 bodies — you have to **separate** them. Splitting a 24 into 12 + 12 destroys half their combat power without a single kill. Frontline's maps hand you the weapon: multiple simultaneously active objectives. Every objective you credibly threaten forces a detachment.

**This reframes objectives entirely: objectives are not just income, they are a dispersion machine.** Threaten three, and an enemy who responds to all three is defeated in detail by whichever two-thirds of your mass you keep together.

### The 7.5 amendment
Because Battle High no longer drops on death, death is now cheap in *power* terms and expensive only in *tempo* (respawn travel) and *rating* (Secure −10, Shatter 8 data to the enemy). Post-7.5 doctrine therefore shifts from "preserve your Battle High above all" to **"preserve your bodies and your position"** — and deliberate aggressive trades at objectives are more defensible than they were before 7.5. Job-swapping still zeroes Battle High and remains its own category of self-inflicted failure.

---

## Part 9 — Concentration, the reserve, and interior lines

### The Schwerpunkt
Clausewitz's centre of gravity (*Schwerpunkt*) is "the hub of all power and movement, on which everything depends" — "the point against which all our energies should be directed." Doctrine demands you name **one** and put everything on it: *"MID PILLAR, EVERYONE, NOW."* Everything else is economy of force.

### The Floating Squad (the decisive reserve)
The most alien concept in pub Frontline and the highest-value one. Keep **6–8 players permanently uncommitted.** The reserve has three doctrinal jobs:

- **Security** — the third team *will* arrive at every fight; the reserve plugs the flank the main body cannot see.
- **Exploitation** — a won fight is worthless unconverted. The main body breaks them; the reserve takes the objective while they are broken. *"You cannot hit the enemy with effect unless you have first created the opportunity; you cannot make that effect decisive unless you exploit the second opportunity that comes before he can recover."*
- **Counter-punch** — the reserve strikes while the enemy is committed to your main body, which is the only moment a six-man group can beat a ten-man group.

A team with a reserve beats a team of identical skill without one, every time.

### Interior lines and the pivot
Jomini defined **interior lines** as those which let a commander "concentrate the masses and maneuver with his whole force in a shorter period of time than it would require for the enemy to oppose to them a greater force." In battlefield terms, interior lines allow more rapid concentration of firepower and manpower, and greater tactical flexibility, letting a numerically inferior force achieve local superiority.

The **central position** is a force multiplier because you can reinforce any front faster than the enemy can concentrate against you. In Frontline:

- **Secure:** the mid-ring plus the pillar is the pivot. Holding it means reaching either flank objective before the enemy can — so mid control is worth *more than its tick rate*.
- **Triumph:** the central gully is the pivot and the ranged high ground. Own it and you can shift to any triumph; lose it and you spend the match on exterior lines.
- **Onsal:** the centre is where S-ranks spawn, so the centre is the income source *and* the pivot.
- The corollary holds in reverse: **exterior lines are a trap.** Attacking both flanks at once divides you into fractions the enemy can crush successively.

---

## Part 10 — The indirect approach: winning without the fight

Liddell Hart, building on Sun Tzu's *cheng* (direct/fixing) and *ch'i* (indirect/striking) forces: **"Dislocation is the aim of strategy; its sequel may be either the enemy's dissolution or his easier disruption in battle."** And: *the greater the psychological surprise and dislocation, the greater the victory.* Dislocation is physical (separate them, endanger their supply and retreat routes) and psychological (induce the feeling of being trapped).

Liddell Hart's study of 280 campaigns across 25 centuries found that only **six times** did a decisive result follow a plan of **direct** strategic approach to the enemy's main army.

### Trade the Centre for the Ring
The centre objective on Onsal, Triumph and Secure is the **line of greatest expectation** — expected, contested, and the site of the three-way stalemate that consumes most of a pub match. Doctrine says the **line of least expectation** and **line of least resistance** lie elsewhere. Deliberately cede the S-rank glory objective and take **three mid-tier objectives simultaneously**: the rate you accumulate while 30 players fight over one S-ovoo will out-produce it, and they will feel entitled to a win they are not earning.

### The Rear-Ring Raid
Liddell Hart: endanger the enemy's **lines of retreat** and rear. Every map has objectives near each base that teams consider "safe" and therefore under-defend. Mount a squad, ride the flank, take the enemy's home-side nodes while their main body is forward — with one caveat: **their respawns emerge at the landing platform right behind you**, with 10 seconds of Invincibility when they leave it. Doctrine: **raid, don't occupy.** You are buying a 60-second income spike and forcing a change of front, not a permanent holding.

### The Anvil and the Hammer (*cheng* / *ch'i*)
Formalise the split: **roughly one third of your force fixes** (visible, engaged, absorbing attention) while **two thirds strike** the enemy's exposed fraction. This is classical defeat in detail, and it is a different play from the death ball — it is the death ball applied to the enemy's weakest piece rather than their centre.

**Defeat in detail**, in its original form, is "to place masses of your army in contact with fractions of your enemy": contain one fraction with a detachment while falling on the other with the bulk of your forces. This is economy of force applied offensively.

### The Ghost Flank (deception)
Sun Tzu: **"All warfare is based on deception. Hence, when able to attack, we must seem unable; when using our forces, we must seem inactive; when we are near, we must make the enemy believe we are far away; when far away, we must make him believe we are near."** And: *"Hiding order beneath the cloak of disorder is simply a question of subdivision."*

Frontline enforces a beautiful, exploitable rule: **the enemy map only shows players within sight range of their own units.** Therefore:

- **Manufacture strength.** Eight players riding in a tight visible column read as a 20-man push. The enemy commits to defend; you do not go.
- **Manufacture absence.** Hold your main body out of sight behind terrain while two players show themselves; the enemy assumes the rest is where the two are.
- **Ghost flank.** A squad visibly rides toward objective A, turns at the last moment, and hits objective C.

In an MMO with 72 players and no voice comms between teams, **the enemy's only sensor is the map.** Deception has an unusually high return here, and almost nobody uses it.

---

## Part 11 — Time: the OODA loop and pre-loading

John Boyd's **OODA loop** — Observe, Orient, Decide, Act — holds that the aim is to **operate inside the adversary's decision cycle**, to "change the situation more rapidly than the opponent can comprehend," forcing him to re-observe, re-orient, re-decide and re-act. Getting inside the enemy's time cycle **inflicts disorder upon him**. Timing and tempo are not about out-speeding an opponent for its own sake — the point is to make his orientation fail.

### The Pre-Load
Frontline has **publicly known timers**:

- Shatter: small ice always activates at **12:30 and 4:30** remaining.
- Triumph: snow at **~16:00**, auroras at **~9:00** (higher triumph ranks + Limit Break gauge fills for everyone).
- Secure: the weaponry timer is on the HUD, and teleport pads go live **30 seconds** before the spawn.

Doctrine: **be standing on the objective before it becomes an objective.** You win the fight before it starts, because the enemy's decision cycle begins when the marker appears and yours began 30 seconds earlier. Pre-declare the rotation in chat: *"at 9 minutes we are all on the gully."*

### The Sunk-Cost Strike
To *break* their loop, attack a team at the exact moment it has committed to an objective. Their decision becomes forced: disengage and forfeit what they have already paid for, or stay and eat the fight. **A choice between two losses is the ideal strategic attack** — it is the only way to make an enemy fight on your terms while you keep the initiative.

---

## Part 12 — The culminating point, and the pursuit that loses matches

Clausewitz: the attacker's superiority **diminishes as the attack advances**, until he reaches the **culminating point of the attack** — the point at which "the superior strength of the attack... is just enough to maintain a defense and wait for peace." Beyond it, "the scale turns and the reaction follows with a force that is usually much stronger than that of the original attacker."

The correlated **culminating point of victory**: moral and physical superiority gained through a successful battle generally augments the victor's strength — *but only to a certain extent.*

### Break Contact on Victory
The most common way of throwing away a won fight in Frontline is **the pursuit**. Chase the enemy back toward their landing platform and you have passed your culminating point: strung out, wounded, out of cooldowns, and now facing **fresh respawns with 10 seconds of Invincibility** streaming off the platform.

Doctrine: **stop at the objective line.** The won fight was for the objective, not for their bodies. Take the node, remount, redeploy.

### Never reinforce failure
If a fight is going badly, more bodies feeds the enemy Battle High — and on Secure, feeds their rating. Accept the loss and spend those bodies on an undefended objective. Liddell Hart's formulation of the same rule: **reinforce success, never failure.** Trickling in is the enemy defeating *you* in detail.

---

## Part 13 — Coalition dynamics: how to play 1st, 2nd and 3rd

A three-way game is not a two-way game. Game theory and history agree: **at each stage, the weakest players align against the strongest player** — alliances form to restore the balance of power. There is a documented *paradox of power* in which a player can suffer from being "too strong," because a runaway leader becomes everyone's target.

Applied to Frontline:

**If you are 1st — the Quiet Leader.** Accumulate quietly, hold what you have, **stay out of the centre melee**, and never present a single clumped mass that invites a 2-vs-1 pinch. A leader who farms in the open converts a won game into a 2v1. Your enemy is **the clock**, not the other teams.

**If you are 2nd — attack the leader's rate, not their existence.** Your enemy is 1st's income. Deny their objectives and pinch them when they are engaged. The biggest mistake 2nd place makes is helping annihilate 1st for free, which simply crowns 3rd.

**If you are 3rd — you need chaos.** Your enemy is **the stalemate**. Seek to create and prolong fights between the other two, then sweep objectives while they grind. Let them fight: every minute two enemies spend killing each other is a minute of uncontested points for a team that is elsewhere.

---

## Part 14 — The 14 named plays

| # | Play | Doctrine source | In one line |
|---|---|---|---|
| 1 | **The 4× Rule** | Lanchester | Count before you engage; 2:1 numbers is 4:1 power |
| 2 | **The Defile** | Lanchester (linear law) | When outnumbered, fight where fire cannot concentrate |
| 3 | **The Split Forcing** | Lanchester inverted | Objectives are a dispersion machine; threat forces detachment |
| 4 | **The Schwerpunkt** | Clausewitz | Name one decisive point and put everyone on it |
| 5 | **The Floating Squad** | Economy of force / security | 6–8 uncommitted players win matches |
| 6 | **The Pivot** | Jomini, interior lines | Own the central position; reach every front first |
| 7 | **Trade the Centre for the Ring** | Liddell Hart, indirect approach | Cede the contested S-rank; take three mid-tier objectives |
| 8 | **The Rear-Ring Raid** | Liddell Hart, lines of retreat | Hit the nodes they consider safe — then leave |
| 9 | **The Anvil and the Hammer** | Sun Tzu, *cheng* / *ch'i* | One third fixes, two thirds strike the exposed fraction |
| 10 | **The Ghost Flank** | Sun Tzu, deception | The enemy's only sensor is the map; lie to it |
| 11 | **The Pre-Load** | Boyd, OODA | Be on the objective before it becomes an objective |
| 12 | **The Sunk-Cost Strike** | Boyd, breaking the loop | Attack the moment they commit; force a choice between two losses |
| 13 | **Break Contact on Victory** | Clausewitz, culminating point | Stop at the objective line; never pursue to their spawn |
| 14 | **The Quiet Leader** | Coalition dynamics | As 1st, look weak and stay unc lumped; as 3rd, create chaos |

**Expanded:**

1. **The 4× Rule** — Before any engagement, count. ≥1.5× their numbers: engage fully and immediately, because half-commitment wastes the square-law advantage you paid for. Roughly even: do not take the fight, take the objective — walk past them. Outnumbered: do not engage at all; bait, delay, withdraw toward allies. Doubling the enemy's numbers quadruples their damage output and quarters your survival.
2. **The Defile** — The square law needs open ground where fire can concentrate. When outnumbered, fight in corridors, corners, stairwells and narrow ramps. You are converting their n² into n¹. This is the only sound way a smaller group beats a larger one, and it is why pursuing a routed enemy into a bottleneck is a gift to them.
3. **The Split Forcing** — You do not need to kill their 24, you need to separate them. Splitting 24 into 12 + 12 destroys half their combat power with no kills. Threaten three objectives credibly and whoever answers all three is beaten in detail. Objectives are not just income; they are a dispersion machine.
4. **The Schwerpunkt** — Name one decisive point per phase and put the mass on it: "MID PILLAR, EVERYONE, NOW." Anything else is economy of force. Rotate the schwerpunkt on the timer, never opportunistically.
5. **The Floating Squad** — Six to eight players permanently uncommitted. They plug the flank the third team always attacks, convert a won fight into a captured objective, and counter-punch while the enemy is committed to your main body. This is the single highest-value habit a caller can institute.
6. **The Pivot** — Hold the central position on the map and you can reach any front faster than the enemy can concentrate against you. On Secure that is the mid-ring plus the pillar; on Triumph it is the gully; on Onsal it is the centre where the S-ranks spawn. Attacking on both flanks simultaneously (exterior lines) divides you into crushable fractions.
7. **Trade the Centre for the Ring** — The centre objective is the line of greatest expectation and eats most of a pub match in a stalemate. Cede it deliberately and take three flanking objectives at once. You will out-produce the melee while its participants believe they are winning.
8. **The Rear-Ring Raid** — Take the nodes near the enemy base that they consider safe. Mount, ride the flank, take the objective, withdraw before their respawns arrive with fresh Invincibility. Raid, do not occupy.
9. **The Anvil and the Hammer** — Split into roughly one third fixing (visible, engaged, absorbing attention) and two thirds striking the exposed enemy fraction. This is defeat in detail: contain one portion while destroying another.
10. **The Ghost Flank** — Because the enemy map only shows what their units can see, eight riders can read as twenty. Feint visibly at objective A, turn, hit objective C. Also: keep the main body out of sight while two players are visible, to make the enemy misplace the rest of you.
11. **The Pre-Load** — Use the public timers (Shatter 12:30/4:30, Triumph 16:00 snow and 9:00 auroras, Secure weaponry + pads 30s early). Be standing there before the marker appears. Pre-declare rotations in chat.
12. **The Sunk-Cost Strike** — Attack exactly when the enemy has committed to an objective. Their choice becomes losing the objective or losing the fight; either way you own the initiative.
13. **Break Contact on Victory** — Stop at the objective line. Pursuit past your culminating point runs you into respawns with Invincibility. Take the node, remount, redeploy. And never reinforce a losing fight — that is how the enemy defeats you in detail.
14. **The Quiet Leader** — As 1st, accumulate without clumping and stay out of the centre; a visible runaway leader is a 2-v-1 waiting to happen. As 3rd, manufacture chaos between the other two. As 2nd, attack the leader's income but keep the third team alive as a distraction.

---

## Part 15 — The call sheet (command structure)

Doctrine is worthless without a command structure. Simplicity demands one-clause orders; unity of command demands one voice.

| Element | Size | Composition | Mission |
|---|---|---|---|
| **Command** | 1 | whoever will speak confidently | declares objective and posture; says nothing else |
| **Scouts** | 2 | mounted mobility jobs | maintain sight-range contacts so the map shows what is actually there |
| **Main body** | 14–16 | tanks and melee (they take −40% to −55% damage) | the schwerpunkt: holds the pivot, wins the set-piece fight |
| **Floating squad** | 6–8 | burst melee plus a healer | reserve: exploit wins, plug flanks, counter-punch |

**Standing orders** (short, unambiguous, announced *before* they are needed):

`REGROUP <place>` · `PUSH <objective> NOW` · `HOLD` · `BAIL` · `PINCH INCOMING <direction>` · `FLOAT` · `NO CHASE`

**Rules of engagement as a decision tree:**

1. Count first. **≥1.5× →** engage completely and immediately.
2. **Even →** do not fight; take the objective and make them come to you on your ground.
3. **<1× →** bait, delay, disengage *toward allies* (never toward base), and look for a defile.
4. **Won the fight →** stop, remount, take the objective. No pursuit.
5. **Losing a fight →** do not reinforce it. Redeploy.

**Two more caller habits:**

- **Two scouts minimum, mounted.** Remember the map only shows enemies within friendly sight range — treat the absence of enemy triangles as *unknown*, not *safe*.
- **Declare disengagements early.** Calling "BAIL" one GCD before you need to is worth more than calling it perfectly at the last moment.

---

## Part 16 — The doctrinal error checklist

Each of these is a *named* violation. Calling them out in chat actually corrects pub behaviour.

| Error | Violated principle | Cost |
|---|---|---|
| 8/8/8 auto-split | Mass | the enemy applies Lanchester to each third in turn |
| Zerging off-objective for kills | Objective | you are farming the means, not the score |
| No reserve | Security | guaranteed pinch from the third team |
| Silence / six competing plans | Unity of Command | every second of indecision is a second of enemy income |
| Marching into the contested centre | Manoeuvre / indirect approach | fighting their fight on their ground |
| Chasing to the landing platform | Culminating point | you lose the fight you already won |
| Trickling back in after a wipe | Economy of force | you are being defeated in detail |
| Job-swapping after building Battle High | (mechanic) | Battle High zeroed, self-inflicted |
| 1st place brawling in the open | Coalition dynamics | you invite a 2-v-1 and hand the game to 3rd |
| Trickling into a three-way stalemate | Simplicity | a resource sink with no reachable objective |
| Treating empty map squares as safe | Security | the map only shows enemies someone can see |

---

## Part 17 — Posture by match phase

| Phase | Posture | Objective |
|---|---|---|
| **0:00–4:00** (approach) | Asymmetric, cautious | Farm Battle High on stragglers; take the *safe* objective; never commit the reserve |
| **4:00–14:00** (main battle) | Mass plus pivot | Hold the interior position; contest the centre **only** as a 2-v-1 against the leader |
| **14:00–20:00** (decision) | Dislocate or protect | If leading: quiet accumulation, no open melee. If behind: force the leader to split, no over-extension |

**The framing question that resolves most mid-match arguments:** *who is your enemy right now?*

- 1st place → your enemy is **the clock**.
- 2nd place → your enemy is **1st's rate**.
- 3rd place → your enemy is **the stalemate**.

---

## Part 18 — Quick reference card

**Engagement gate:** ≥1.5× numbers engage · even → take the objective · fewer → disengage.

**Battle High:** max 100 · +10% damage and healing per 20 · BH V is announced match-wide · 7.5: no loss on death · **job change resets it.**

**Kill value:** victim's BH tier at 4/6/8/12/16/20 (KO) or 2/3/4/6/8/10 (assist).

**Limit Break:** 1st place +25% slower charge · 3rd place +25% faster.

**Survivability:** tanks/melee −40% to −55% damage taken; ranged/casters −25% to −35%.

**Map rules:** 72 players · 20 minutes · 24 per team · premade max 4 · random Grand Company · 10s Invincibility on leaving the landing platform · any hit dismounts you and applies uncleansable Hoofing It.

**Thresholds:** Secure 2,400 (node breakpoint at **4**) · Seize 700 data (lowered from 800 in 6.4 — verify on the HUD) · Shatter 1,600 data (KO = 8; small ice caps 50, large 200) · **Onsal 1,400** · Triumph 1,400.

**Ovoo payout (Onsal):** B 50 · A 100 · S 200, paid at **5 / 10 / 20 per 3 seconds over 30 seconds** — a claim is worth `rate × time left`, capped at the rank total. KO +8 · death −8 (flat; a 16-point swing).

**Timers:** Shatter small ice at 12:30 and 4:30 remaining · Triumph snow ~16:00, auroras ~9:00 · Secure teleport pads live 30s before weaponry spawn.

**Secure mid values:** Nodes +150 · α drones +30 · Command Systems +24 · drones +10 · KO +10 · death −10.

**Secure node rate per 3s:** 1→2, 2→4, 3→6, **4→10**, 5→12, 6→14, 7→18, 8→20, 9→22.

**Triumph capture:** one player per field; extra bodies do not speed it; **any enemy inside a field blocks it**; claimed triumphs cannot be seized.

---

## Sources

**Game mechanics**

- [Frontline — Final Fantasy XIV Online Wiki](https://ffxiv.consolegameswiki.com/wiki/Frontline) (KDA, Battle High, job modifiers, Limit Break charge times, landing platform, mounts, map, rewards)
- [The Borderland Ruins (Secure) — FFXIV Online Wiki](https://ffxiv.consolegameswiki.com/wiki/The_Borderland_Ruins_(Secure))
- [Seal Rock (Seize) — FFXIV Online Wiki](https://ffxiv.consolegameswiki.com/wiki/Seal_Rock_(Seize))
- [The Fields of Glory (Shatter) — FFXIV Online Wiki](https://ffxiv.consolegameswiki.com/wiki/The_Fields_of_Glory_(Shatter))
- [Onsal Hakair (Danshig Naadam) — FFXIV Online Wiki](https://ffxiv.consolegameswiki.com/wiki/Onsal_Hakair_(Danshig_Naadam))
- [Worqor Chirteh (Triumph) — FFXIV Online Wiki](https://ffxiv.consolegameswiki.com/wiki/Worqor_Chirteh_(Triumph))
- [Role Actions (PvP) — FFXIV Online Wiki](https://ffxiv.consolegameswiki.com/wiki/Role_Actions_(PvP))
- [Frontline — The Lodestone play guide](https://na.finalfantasyxiv.com/lodestone/playguide/contentsguide/frontline/)
- [Worqor Chirteh (Triumph) — The Lodestone](https://na.finalfantasyxiv.com/lodestone/playguide/contentsguide/frontline/6/)
- [Patch 7.2 notes (Secure rework, role actions)](https://na.finalfantasyxiv.com/lodestone/topics/detail/3c4910f373e497acd3428c37f6358e341e4cc06d/)
- [Patch 7.4 notes (Triumph added)](https://na.finalfantasyxiv.com/lodestone/topics/detail/06944d892fd98cc00b2a28ff77edbafa4f7eef54/)
- [Patch 5.18 notes — Naadam rating 1,800 → 1,600, KO/death value 10 → 8 (JP Lodestone)](https://jp.finalfantasyxiv.com/lodestone/topics/detail/f586b313e4f6c76c0cc18d99fc15c6058bb0f5ee)
- [Patch 6.4 notes — Naadam rating 1,600 → 1,400; **Seize data 800 → 700**; Shatter data 1,600 → 2,000 with Allagan tomeliths removed from Shatter](https://www.ign.com/wikis/ffxiv/FFXIV_6.4_The_Dark_Throne_Patch_Notes_and_Release_Date)
- [Patch 6.55 notes — Shatter ice timers: first small ice 420 s, reactivation 420 s, destroyed small reappears 360 s, destroyed large respawns 60 s, 15 small and 2 large active at once; max HP 300,000 / 3,000,000](https://na.finalfantasyxiv.com/lodestone/topics/detail/012d8e96b662a92eb4405c25b9958184db248348)
- [Shatter patch history including 6.57 (Shatter data back to 1,600, KO 5 → 8) and the 6.4 rework — FF14 Online Wiki](https://ff14wiki.info/?%E3%83%95%E3%82%A3%E3%83%BC%E3%83%AB%E3%83%89%E3%83%BB%E3%82%AA%E3%83%96%E3%83%BB%E3%82%B0%E3%83%AD%E3%83%BC%E3%83%AA%E3%83%BC)
- [Seize tomelith cadence: four activate 30 s after the start, each lasting a random 2 to 3 minutes — 攻略:ark](https://ff14a.net/pvp-seal-rock.php)
- [Seize 6.5 rules: 700 to win, a drained tomelith replaced after about 15 s, spawn count falls and rank rises as the match runs — うわさの調べ](https://uwasablog.com/game230406/)
- [Seal Rock (Seize) strategy, incl. the 600-plus endgame — FFXIV Online Wiki](https://consolegameswiki.com/wiki/Seal_Rock_(Seize)_Strategy)
- [うわさの調べ — フロントラインの各ルール簡易解説【6.5】](https://uwasablog.com/game230406/) (ovoo tick rates, 30-second payout, no re-claiming)
- [ララのおもちゃ箱 — オンサルハカイルの基礎](https://lala-toybox.com/pvp/flontline/onsal/) (rank payout table)
- [INUISM — 【FL】オンサル・ハカイル(終節戦)](https://inuism.com/ff14_fl_onsalhakair) (score sources, KO ±8)
- [巴哈姆特 — 72人！オンサル・ハカイル](https://forum.gamer.com.tw/C.php?bsn=17608&snA=15282) (phase composition, three-team endgame doctrine)
- [Live Letter 86 summary — patch 7.2 PvP](https://novacrystallis.com/2025/03/final-fantasy-xiv-live-letter-86-summary-patch-7-2-arrives-march-25-2025/)

**Player strategy**

- [AkhMorning — FFXIV Frontline guide](https://www.akhmorning.com/pvp/frontline/)
- [r/ffxiv — How to greatly improve your odds of winning Frontlines](https://www.reddit.com/r/ffxiv/comments/qi6bc6/how_to_greatly_improve_your_odds_of_winning/)
- [r/ffxiv — Olivia's Updated Frontline Guide 7.1](https://www.reddit.com/r/ffxiv/comments/1id3d9a/olivias_updated_frontline_guide_71/)
- [r/ffxiv — Worqor Chirteh (Triumph) discussion](https://www.reddit.com/r/ffxiv/comments/1pxax9h/worqor_chirteh_triumph_the_new_frontline_map_is/)
- [Late to the Party Finder — Onsal Hakair (Danshig Naadam)](https://latetothepartyfinder.com/ffxiv-onsal-hakair-danshig-naadam/)
- [Red Bull — How to master the battlefield of FFXIV's PvP daily duty](https://www.redbull.com/ca-en/final-fantasy-14-frontlines-pvp-guide)

**Military doctrine**

- [The nine principles of war (MOOSEMUSS) — DTIC](https://apps.dtic.mil/sti/tr/pdf/ADA503932.pdf)
- [What is military strategy? (Oxford Academic) — principles of war](https://academic.oup.com/book/57480/chapter/466865884)
- [Lanchester's laws](https://en.wikipedia.org/wiki/Lanchester%27s_laws)
- [Force concentration (square-law worked examples)](https://en.wikipedia.org/wiki/Force_concentration)
- [The Designer's Notebook: Lanchester's Laws](https://www.gamedeveloper.com/design/the-designer-s-notebook-kicking-butt-by-the-numbers-lanchester-s-laws)
- [Clausewitz: fog, friction, centre of gravity, culminating point](https://www.globalsecurity.org/military/library/report/1991/HHT.htm)
- [Clausewitz and his treatise On War](https://www.lebarmy.gov.lb/en/content/clausewitz-and-his-treatise-war-and-its-relevance-21st-century)
- [Centers of gravity and strategic planning (Army University Press)](https://www.armyupress.army.mil/Journals/Military-Review/English-Edition-Archives/January-February-2022/Metz-Centers-Gravity-1988/)
- [Liddell Hart, Strategy (1954) — dislocation and the indirect approach](https://classicsofstrategy.com/2016/01/19/liddell-hart-strategy-1954/)
- [The Indirect Approach — Strategy: A History](https://erenow.org/ww/strategy-a-history/12.php)
- [Boyd's OODA Loop — operating inside the decision cycle](https://www.mca-marines.org/wp-content/uploads/Let-Boyd-Speak.pdf)
- [Interior lines (Jomini)](https://en.wikipedia.org/wiki/Interior_lines)
- [FMFRP 12-13, Maneuver in War — Napoleon, interior lines, defeat in detail](https://www.marines.mil/Portals/1/Publications/FMFRP%2012-13%20%20Maneuver%20in%20War.pdf)
- [The Art of War — Sun Tzu (MIT Classics)](https://classics.mit.edu/Tzu/artwar.html)
- [Endogenous formation of alliances in conflicts — balance of power](https://sites.socsci.uci.edu/~mrgarfin/OUP/papers/Bloch.pdf)
- [Too Big to Prevail: The Paradox of Power in Coalition Formation](https://www.ifo.de/DocDL/cesifo1_wp8980.pdf)
