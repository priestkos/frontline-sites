# FFXIV Frontline — Jobs, Roles, and How They Interact

**Companion to `ffxiv-frontline-complete-guide.md`.** That guide's Part 5 is a summary; this is the full workup.

Reference patch: **7.5**. Job balance in Frontline is re-tuned most patches. The *framework* here (roles, role actions, the kill chain, counter-pairs) is stable; the *rankings* are a snapshot.

Reliability note up front: per-job claims below come from a Japanese Frontline commander's 7.5 job analysis (6,972 matches, 42% win rate) and a second JP practitioner's per-role series, cross-checked against the consolegameswiki for every number. Where an English-language tier list disagrees, the disagreement is stated rather than averaged.

---

## Table of contents

- [Part 1 — There are five roles, and the role is not the job](#part-1)
- [Part 2 — The durability ladder: damage-taken modifiers](#part-2)
- [Part 3 — Role actions: the fifteenth ability](#part-3)
- [Part 4 — How the roles interact: the kill chain](#part-4)
- [Part 5 — Counter-pairs: what beats what](#part-5)
- [Part 6 — Three-team geometry, and what each role does about it](#part-6)
- [Part 7 — The 21 jobs, role by role](#part-7)
- [Part 8 — Map affinity matrix](#part-8)
- [Part 9 — Job selection strategy](#part-9)
- [Part 10 — Tier lists, and how much to trust them](#part-10)
- [Sources](#sources)

---

<a id="part-1"></a>
## Part 1 — There are five roles, and the role is not the job

Twenty-one jobs, five roles:

| Role | JP name in chat | Jobs | Count |
|---|---|---|---|
| **Tank** タンク | タンク *tanku* | Paladin ナイト, Warrior 戦士, Dark Knight 暗黒騎士, Gunbreaker ガンブレイカー | 4 |
| **Healer** ヒーラー | ヒーラー *hīrā* | White Mage 白魔導士, Scholar 学者, Astrologian 占星術師, Sage 賢者 | 4 |
| **Melee DPS** 近接物理DPS | メレー *merē* | Monk モンク, Dragoon 竜騎士, Ninja 忍者, Samurai 侍, Reaper リーパー, Viper ヴァイパー | 6 |
| **Physical Ranged DPS** 遠隔物理DPS | レンジ *renji* | Bard 吟遊詩人, Machinist 機工士, Dancer 踊り子 | 3 |
| **Magical Ranged DPS** 遠隔魔法DPS | キャスター *kyasutā* | Black Mage 黒魔導士, Summoner 召喚士, Red Mage 赤魔導士, Pictomancer ピクトマンサー | 4 |

**What the role actually decides** — exactly three things:

1. **Which role action you may equip.** Every role has its own pool of three, and you pick one. A Dancer can never take Rampart.
2. **Your damage-taken modifier.** Tanks and melee take sharply less damage than ranged; this is the single biggest determinant of whether you can stand in a Frontline fight.
3. **The rough shape of your kit** — HP pool, whether your damage needs you in melee range, whether you have a barrier.

**What the role does *not* decide: your battlefield function.** This is the most important thing in this document, and the reason tier lists look contradictory. In Frontline:

- **Paladin is not a tank.** It is the highest-burst job in the game (see Part 7). The commander's own line: "もはやメレーと考えた方がいい" — *think of it as a melee*.
- **Sage is not a healer.** It is a pull-and-burst assassin with a 25-yalm blink. "断じてヒーラーではない" — *it is decidedly not a healer*.
- **Scholar is not a healer either**, and its healing is the weakest of the four; it is a DoT-pressure and shield-support job that cannot participate in a burst window.
- **Bard is not a fragile ranged job.** With its role action it out-survives most melee — "メレーを超える耐久" — and its job is to make one ally monstrous.
- **Red Mage fights in melee range on purpose** and takes damage like a melee job.
- **Monk and Samurai behave like tanky bruisers**; Samurai's cooldown is a 4-second tank button.

So: **read the job, not the role.** The role tells you your role action and your damage-taken modifier and nothing else.

---

<a id="part-2"></a>
## Part 2 — The durability ladder: damage-taken modifiers

Frontline applies a job-specific multiplier to incoming damage. The bands:

| Band | Jobs | Reported values |
|---|---|---|
| **Melee + tanks** | PLD, WAR, DRK, GNB, MNK, DRG, NIN, SAM, RPR, VPR | roughly **−40% to −55%** damage taken |
| **Ranged (physical + magical)** | BRD, MCH, DNC, BLM, SMN, RDM, PCT | roughly **−25% to −35%** |

Individual values reported by the 7.5 JP analysis:

- **Paladin — 45%**, which the commander calls *low for a melee*, and therefore **unsuited to absorbing damage like a tank**. Paladin's mitigation is deliberately the shallowest in the melee band; if you want to be the wall, this is the wrong job.
- **Red Mage — 45%**, called *excellent for a ranged*. Red Mage sits at or above the top of the ranged band, so it can stand in melee range and brawl.
- **Sage — high for a ranged, only about 5% below Dark Knight.** A ranged job with near-melee mitigation, plus barriers. That is why Sage dives.

Two consequences that decide matches:

1. **A ranged job focused by three people dies in a global cooldown or two.** Positioning is not a preference for ranged jobs, it is the entire skill.
2. **The anvil of a Frontline fight is the melee+healer mass**, not the DPS. Whoever can hold space longest decides where the next fight happens.

Modifiers are also applied to **damage dealt** on some jobs — Dragoon and Warrior both carry *reduced* damage output in Frontline (Dragoon's is the famous "main-character tax" 主人公補正), and these corrections are why the PvE tier list does not transfer.

---

<a id="part-3"></a>
## Part 3 — Role actions: the fifteenth ability

**Added in patch 7.2.** Each role gets **three**, and you equip **exactly one**. They are only usable in Frontline, Rival Wars, and the Wolves' Den Pier, and **can only be changed in the spawn area** — i.e. before the gates open.

### Tank

| Action | Effect | Recast |
|---|---|---|
| **Rampage** ランページ | 8,000 potency to all nearby enemies (10y), **+25% damage taken by targets**, 10s | 45s |
| **Rampart** ランパート | **−50% damage taken**, +25% HP recovery, 15s | 60s |
| **Full Swing** フルスイング | 8,000 potency, **30-yalm knockback, removes Guard** | 30s |

### Melee DPS

| Action | Effect | Recast |
|---|---|---|
| **Bloodbath** ブラッドバス | **+25% damage dealt, 100% of damage dealt converted to HP**, 10s | 45s |
| **Swift** スウィフト | **+100% movement speed, immunity to Stun/Heavy/Bind/Silence/Sleep/Deep Freeze/knockback/draw-in**, 4s | 30s |
| **Smite** スマイト | 6,000 potency rising to **18,000 at ≤25% HP**, **ignores Guard**, **recast resets on KO or assist** | 15s |

### Physical Ranged DPS

| Action | Effect | Recast |
|---|---|---|
| **Dervish** スピードスター | −10% cast and recast, **+33% movement speed for self and nearby party**, 12s, crosses cover | 45s |
| **Bravery** ブレイブ | **+25% damage dealt AND −25% damage taken**, 15s, 30-yalm range (can self-cast) | 30s |
| **Eagle Eye Shot** イーグルアイ | **12,000 potency, ignores Guard**, 40-yalm range | 15s |

### Magical Ranged DPS

| Action | Effect | Recast |
|---|---|---|
| **Comet** コメット | **20,000 potency AoE**, 2.4s cast you **cannot move or cancel** during | 45s |
| **Phantom Dart** ファントムダート | 4,000 potency, **+25% damage taken by the target**, 5s | 15s |
| **Rust** ダルウェポン | **−33% damage dealt AND healing potency** on target + nearby enemies, 10s | 30s |

### Healer

| Action | Effect | Recast |
|---|---|---|
| **Haelan** ヒール | Restore HP, 16,000 potency (8,000 on self), 2,000 MP | 2.4s |
| **Stoneskin II** ストンラスキン | **Barrier worth a 12,000-potency heal** for self + nearby party, 10s, crosses cover | 30s |
| **Diabrosis** ディアブロシス | 9,000 potency AoE, **−33% HP recovered by healing actions** on the target, 10s | 45s |

### What the JP community actually equips

A 6,972-match practitioner's per-job ratings (◎ = "just take it", × = "never"):

| Job | Best pick | Notes |
|---|---|---|
| **PLD** | **Rampage** (Rampart ×) | Rampart is wasted on a job that isn't a tank |
| **WAR** | **Rampage** | |
| **DRK** | **Rampage** or **Rampart** | Rampart when commanding and expecting focus |
| **GNB** | **Rampage** or **Rampart** | Rampart for the stable wall build |
| **DRG** | **Bloodbath** or **Smite** | Bloodbath is what pulled Dragoon back into relevance |
| **MNK** | **Smite** | |
| **NIN** | **Smite** | |
| **SAM** | **Bloodbath** or **Smite** | Bloodbath stacks with the job's own recovery |
| **RPR** | **Swift** | A rare job where Swift is the pick, to land the LB |
| **VPR** | any of the three | All rated top |
| **WHM / SCH / AST / SGE** | **Diabrosis** | Unanimous first choice for every healer |
| **BRD** | **Bravery** | |
| **MCH** | **Bravery** or **Eagle Eye Shot** | Eagle Eye suits Machinist's thin attack kit |
| **DNC** | **Bravery** (Dervish also fine) | |
| **BLM** | **Phantom Dart** | "Take it on Shatter for breaking ice" |
| **SMN** | any of the three | |
| **RDM** | **Comet** or **Phantom Dart** | |
| **PCT** | **Comet** or **Phantom Dart** | |

**Three role actions are outliers in power:**

- **Bravery** — +25% damage *and* −25% damage taken for 15 seconds on a **30-second** recast. The JP write-up's verdict: *the printed effects are so strong it reads like a Limit Break*. It is why Bard works, and the reason a Bard should be glued to your best melee player.
- **Rampage** — 8,000 AoE with a +25% damage-taken debuff on a 45-second recast. Called *the skill that defines the current environment* — it turns any coordinated burst into a wipe.
- **Smite** — 6,000 → 18,000 potency that **ignores Guard** and **resets on every KO or assist**. This is the single best cleanup tool in the game, and it makes a kill chain self-sustaining.

**The knock-on effect on the maps:** role actions raised total damage so much that Shatter's large ice, which used to take a minimum of ~40 seconds of focused fire, now breaks in as little as ~15. Timings written before patch 7.2 for objective races are optimistic.

---

<a id="part-4"></a>
## Part 4 — How the roles interact: the kill chain

A Frontline kill is not one player doing damage. It is a five-stage chain, and each role owns a stage. If a stage is missing, the fight is a stalemate; if the chain completes, the target dies regardless of skill.

| Stage | What it is | Jobs that do it | The specific tools |
|---|---|---|---|
| **1. Initiation** | Put the enemy where they cannot leave, before they can react | **DRK** (best in the game), WAR, SGE, DNC, RPR, MNK, WHM, BRD | Salt Earth ソルトアース pull+bind (10m, DRK), Primal Rend stun + Blota pull (WAR), Plegma フレグマ pull (SGE), Contra Dance (DNC), Lemore panic (RPR), Meteor Drive (MNK), Heart of Purgation stun (WHM) |
| **2. Amplification** | Raise the damage everyone deals to that target | **Tank, Phys Ranged, Magic Ranged, AST, PCT** | Rampage +25% damage taken (Tank role action), Phantom Dart +25% (Magic ranged role action), Bravery +25% damage dealt (Phys ranged), Astrodyne LB +30% party damage (AST), Star Prism +10% (PCT) |
| **3. Denial** | Remove the defences that would save them | **Tank, Phys Ranged, Melee, Healer** | Full Swing strips Guard (Tank), Smite and Eagle Eye ignore Guard (Melee / Phys ranged), Diabrosis −33% healing received (Healer) |
| **4. Sustain** | Keep the dive alive long enough to finish | **WAR, PLD, GNB, DRK, SAM, MNK, RPR, VPR, WHM, AST, SGE** | Warrior self-heal, Holy Sheltron barrier (PLD), Continuous Blade −25% taken (GNB), Blackest Night barrier (DRK), Chiten 4-second tank window (SAM), Bloodbath lifesteal (Melee role action) |
| **5. Finish** | Kill the half-HP target before help arrives | **NIN** (best), SAM, MCH, DRG, DNC, VPR | Assassinate LB 星遁天誅 (NIN — the strongest pursuit tool in the mode), Zantetsuken (SAM), Magic Bullet LB (MCH), Sky Shatter (DRG), Blade Dance combo (DNC) |

**How to read a losing fight:** find the missing stage.

- Enemies diving you and nobody dies → you have no **amplification** or no **denial**. Take Rampage, Phantom Dart, or Diabrosis.
- Your dive keeps dying at 30% → you have no **sustain**. Guard on the way out, or pick a job with a barrier.
- You keep getting kills but not converting them → you have no **finisher**. That is Ninja's entire purpose.
- You keep getting caught and never get to choose a fight → you have no **initiation**. That is Dark Knight's.

---

<a id="part-5"></a>
## Part 5 — Counter-pairs: what beats what

Some matchups are close to deterministic. Learning five of them is worth more than learning a tier list.

| Threat | What answers it |
|---|---|
| **Samurai holding Zantetsuken** (100% of max HP as damage) | **Barriers.** The LB deals 100% of *maximum* HP and is defeated by HP + barrier exceeding 100%. So: Blackest Night (DRK), Stoneskin II (Healer), Tempera Coat (PCT), barrier skills on MNK/RDM/GNB, Paladin's Guardian on the threatened ally. Never stand in front of a waiting Samurai at 100% HP with no barrier. |
| **Someone Guard-stalling on an objective** | **Full Swing** (removes Guard outright), **Smite**, **Eagle Eye Shot** (both ignore Guard). Three of the five roles have a Guard-answer. |
| **A good healer topping up a deathball** | **Diabrosis** (−33% HP recovered) + **Rampage** (+25% damage taken) + a finisher. Without the healing debuff, damage is a suggestion. |
| **A ranged job that refuses to die** (Bard with Bravery, Sage, Red Mage) | **Rampage + focus with three or more attackers.** Bravery's −25% taken is not immunity; concentrated burst still breaks it. Reduce their support instead: **Rust** (−33% damage dealt) on the damage dealer. |
| **Dark Knight Salt Earth initiation on your backline** | **Purify** on reaction, or pre-emptive **Swift** (Tank/Melee — 4s of CC immunity including draw-ins). Note Purify does **not** cleanse Hoofing It. |
| **Reaper panic + burst** | Spread out. The JP analysis notes the LB's own weakness is that panic **scatters** the enemy team, which can save them. |
| **Warlike Warrior chain-pulling your healer** | Samurai's Chiten (instant Guard-like window) is a documented answer; so is anyone with a barrier and a disengage. |
| **Dragoon's AoE bomb** | It has essentially no crowd control — it wins by damage, so **deny the positioning** rather than the damage: do not stand in a pre-formed clump on the timer. |

---

<a id="part-6"></a>
## Part 6 — Three-team geometry, and what each role does about it

Frontline is not a duel — it is a **three-body problem**, and the third team decides most fights. Role behaviour has to change with your current standing:

- **Whoever is 1st** charges Limit Break **25% slower**, and **3rd charges 25% faster**. So the trailing team's win conditions — big AoE LBs (DRG, DNC, RPR, SAM, DRK) — come online sooner, automatically. A trailing team is not out of the match; it is on a faster clock.
- **A pincer resolves a stalemate.** The standard death wants to be true; the third team's arrival is what punishes it. This is why "do not be the team that commits into the middle" is doctrine.
- **The roles that can disengage are the ones that survive being pinched.** Swift (any melee), Shukuchi (NIN), Dragoon's jumps, Dancer's 4-stack blink, Red Mage's Corps-a-corps, Pictomancer's Smudge, Sage's Ikaros. Jobs with no escape — Machinist, Summoner, Bard, Black Mage — must never be the deepest player on the field.
- **Coalition logic:** as 1st you want the other two to fight each other; as 3rd you never fight 2nd (you need them to overtake the leader). Jobs with strong denial (Rampage, Diabrosis, Full Swing) are the tools for a leading team that must not take fair fights.

---

<a id="part-7"></a>
## Part 7 — The 21 jobs, role by role

Format per role: one table, then notes on the jobs that need them.

### 7.1 Tanks

| Job | Frontline function | Strengths | Weaknesses | Role action | Difficulty |
|---|---|---|---|---|---|
| **Paladin** ナイト | Burst damage dealer wearing plate | **Highest instantaneous burst in the game**; Holy Sheltron barrier auto-fires without consuming a GCD and is amplified by Battle High; Guardian + Phalanx protect allies; passive 3,000-HP-per-hit recovery for anyone hitting marked enemies | **45% damage taken is shallow for a melee**; no real tanking; all-in burst leaves it with nothing to do; barrier can be stripped | Rampage | Medium |
| **Warrior** 戦士 | Initiator + brawler | Many strong CCs; 20-second AoE burst cycle with a stun; Primal Rend + Onslaught catch; self-healing sustain; best tank for beginners | Carries a **damage-dealt penalty** in Frontline — "hard to call it high damage"; healing-first kit is slightly out of step with the BH meta | Rampage | **Easy** |
| **Dark Knight** 暗黒騎士 | The initiator of the mode | **Salt Earth is the best initiation tool in Frontline** — a 10m pull + bind that pairs perfectly with burst; Even Tide is high damage *and* durable; grants barriers to allies; carries games | Heavy nerfs since Endwalker; Purify and Guard now answer the pull; its own blink telegraphs the dive; **squishy without Even Tide or Rampart**; ability-heavy, so it loses GCD uptime | Rampage / Rampart | **Hard** |
| **Gunbreaker** ガンブレイカー | The wall, plus the best LB damage in the game | **Continuous Blade is the highest-total-damage LB**, and grants 25%+ damage reduction while it runs; ソイルコンボ self-barriers; Rampart synergy is the best in the game; hardest job in Frontline to kill | **Weak AoE**; crowd control lives almost entirely on the LB; Continuous Blade is very vulnerable to Samurai's Zantetsuken; precise execution required | Rampage / Rampart | Medium |

> **Paladin's real identity:** it is a burst job. The commander's summary is blunt — Holy Sheltron's barrier explodes for damage, Battle High raises *both* the barrier's size and the damage it deals, so **Paladin scales harder with Battle High than any other job**. Using invulnerability to keep the barrier intact and fire the maximum burst is "the strongest use the developers probably never intended". If you take Paladin expecting to tank, you will do neither job well.

> **The Dark Knight–Reaper pair:** Dark Knight's pull exists to set up someone else's kill; Reaper's single-target damage and its panic LB are the natural follow-up. Nicely, Reaper's job value rose and fell with Dark Knight's across patches, because they are used together.

### 7.2 Healers

| Job | Frontline function | Strengths | Weaknesses | Role action | Difficulty |
|---|---|---|---|---|---|
| **White Mage** 白魔導士 | Ranged CC + burst, with the clearest heals | Simple and readable; **Heart of Purgation's long-range AoE stun is a fight-winner**; LB gives party-wide regen; 8,000-barrier Aquaveil also cleanses a debuff; Seraph Strike buffs allies in melee | Miracle of Nature has been nerfed repeatedly and is now only a silence/MP drain; **fragile** — it can soak a few hits, not a melee's worth | Diabrosis | **Easy** |
| **Scholar** 学者 | DoT pressure + shields | 鼓舞激励 boosts allies' damage and shields; the DoT's damage scales steeply once Battle High is high; powerful in a long attrition line | **No burst whatsoever**; DoT damage is badly under-scaled for a mode decided by burst windows; the fairy is stationary with a small radius in a mode that will not stop moving; **contributes little to a fight's outcome** | Diabrosis | Hard |
| **Astrologian** 占星術師 | The support healer — and the best one | Strong single-target heal plus Macrocosmos AoE heal; **Astrodyne LB gives allies +30% damage dealt** — the single best buff in the mode; excellent AoE damage (Gravira, double-cast); high mobility via Epicycle; cards on demand | Physically the softest job on the field; must step to ~15m to land Macrocosmos | Diabrosis | **Easy** |
| **Sage** 賢者 | Pull-and-burst assassin | **Ikaros is a 25-yalm blink** into Plegma — a pull that, unlike Salt Earth, locks one target deterministically and arrives too fast to react to; Toxicon spreads a damage-taken debuff; heavy barriers; **near-melee damage mitigation for a ranged job** | Its healing method does not suit Frontline and its throughput is poor; if you play it as a support job, you will do nothing all match; more buttons to manage than any other healer | Diabrosis | **Hard** |

> **The healer paradox:** the JP analysis of this patch is unambiguous that **Astrologian is the only healer whose support pays for itself**, that **Sage is not a healer**, and that **Scholar cannot affect a Frontline fight**. White Mage sits in between: its value is the AoE stun and the LB, not the healing. If your team has exactly one healer and it is a Scholar, the team has no healer.

### 7.3 Melee DPS

| Job | Frontline function | Strengths | Weaknesses | Role action | Difficulty |
|---|---|---|---|---|---|
| **Monk** モンク | Single-target bruiser / catch tool | **Meteor Drive LB strips defence *and* locks the target — top-tier catch**; 抜重歩法 gives a barrier plus 3 blinks and is the key to the job; tanky for a DPS; barriers help allies and counter Samurai; Phoenix Dance + Enlightenment chip from range | AoE burst is hard to actually complete; **no stun any more**, so its single-target pursuit is worse than it was; if you cannot use the blink well it feels far softer than it is | Smite | Hard |
| **Dragoon** 竜騎士 | Mobile AoE bomb | **Sky Shatter is the strongest AoE burst in the game** and can erase a clump; unmatched mobility — it can arrive from any angle and leave fast; Horrid Roar lets it briefly act as a tank; Bloodbath (7.5) restored its damage | Carries the **main-character damage penalty** in Frontline; **no crowd control at all** — it wins purely on damage; the LB charges slowly enough to be genuinely annoying | Bloodbath / Smite | Medium |
| **Ninja** 忍者 | Assassin / harasser | **The best finisher in the mode** — the LB 星遁天誅 is unmatched at killing anything that is already half dead or Guard-stalling; strong ranged pokes, CC, self-heal, self-barrier; Shukuchi **drops target lock**, so it can escape what nobody else can; genuinely hard to kill | **Almost no AoE** — it cannot participate in a group burst window; demands that you find half-dead targets rather than create them; a Ninja who only throws ranged attacks contributes nothing | Smite | **Hard** |
| **Samurai** 侍 | Deterrent / objective bully | 火力◎耐久◎機動〇; **Zantetsuken is a one-shot guaranteed-KO effect** on the scoreboard's edge cases; Chiten gives a 4-second tank window on a 4-minute-or-so cooldown lever; excellent at stealing Returns (リス) and displacing people from objectives; may be the best job at scraping the last few points in the final seconds | **Zantetsuken is defeated by any barrier** — HP + barrier above 100% survives it; no backward mobility, so Purify and Guard timing is everything; its pressure is *passive* — it waits for you to be careless | Bloodbath / Smite | Medium |
| **Reaper** リーパー | Panic-button bruiser | Decent durability, plentiful AoE, and **a hard-incapacitate LB**; Harvest Moon is a *ranged AoE that heals*; Death Warrant + Smite is a strong execute pair | **70% of the job is the LB**, and playing that LB well is genuinely difficult; needs a front line to exist or it becomes cramped and useless; strongly dependent on the player's and the team's competence | Swift | Hard |
| **Viper** ヴァイパー | The 7.5 protagonist | **Top-tier burst, mobility *and* durability simultaneously**; Serpent's Scales (蛇鱗術) is a survivability cooldown that also feeds the LB; the LB charges fast and applies Heavy; a 20m poke combo lets it soften targets before committing; best Bloodbath synergy in the game | **No crowd control except the LB's Heavy** — its catch is poor; the big Serpent combo draws enormous attention and dies instantly if played carelessly; the JP analysis notes Viper players suiciding into 24 people is now a recognisable pattern | Bloodbath / Smite | Medium |

### 7.4 Physical Ranged DPS

| Job | Frontline function | Strengths | Weaknesses | Role action | Difficulty |
|---|---|---|---|---|---|
| **Bard** 吟遊詩人 | Force multiplier | **Bravery changes the job's premise**: with +25% damage dealt and −25% taken it becomes a line-fighter, and Wardens Paean on top gives it *more* durability than a melee; Apex Arrow + Hero's Encore is genuinely high damage and burns MP too; Harmonic Arrow is top-tier single-target; Repelling Shot gives a short-recast catch; the LB is a directional knockback | Weak AoE burst outside the Fantasia window; **long recasts and no real blink**; the AoE options are lines that require exposing yourself; the JP analysis is explicit that Bard is **an advanced job that beginners mistake for an easy one** | Bravery | **Hard** |
| **Machinist** 機工士 | Single-target executioner | Excellent at killing anything that is already disengaging or floating — including other ranged jobs; Analyse + Saw + Full Metal Burst + the LB (Magic Bullet) is a reliable kill package on a ranged target; Drill is good against Guard; **the turret is a genuinely strong Return/objective denial tool** | **Almost no AoE burst**; no blink; if caught it cannot escape, so it cannot soak for anyone; the LB is poor against melee; overall it lacks exactly the things Frontline wants (AoE, durability, mobility) | Bravery / Eagle Eye Shot | **Hard** |
| **Dancer** 踊り子 | The best LB in the mode | **Contra Dance is described as the most broken LB in Frontline history** — a 4-second charm/bind that forces the enemy to either burn invulnerability, evade, or commit to killing you; **rated top-tier on all five maps**; Blade Dance combo is instant, high damage and never desynchronises; Brave + Fan Dance makes it surprisingly hard to kill; Closed Position on a frontliner is a big buff; **multiple Dancers in one party is a legitimate composition** | Short 15m range on most skills feels awkward; without Bravery it is just a fragile ranged job; no ordinary CC, so it cannot catch a single target; the follow-up after Contra Dance can get you killed | Bravery (Dervish fine) | **Easy** |

### 7.5 Magical Ranged DPS

| Job | Frontline function | Strengths | Weaknesses | Role action | Difficulty |
|---|---|---|---|---|---|
| **Black Mage** 黒魔導士 | Sustained area damage | **Every AoE hits hard and it never has to stop**; Flare Star's damage and the DoT, or Glacial Star's lockdown, give it two modes; Soul Resonance is available every fight; Etherial Step moves to friend *or* foe; its "burst" spell is a 15,000 barrier so it can be very hard for a moment; Pyretic | **Vanishingly fragile the instant its defensive tools are down**; cast times mean it must stand still in a mode full of knockbacks and pulls; the barrier window is the only time it can be in front | Phantom Dart | Medium |
| **Summoner** 召喚士 | Teaching-friendly area damage | Many clear, strong AoE skills; **Bahamut's range is enormous and the LB is extremely easy to use**; Radiant Aegis gives an ally a 25% damage-taken cut and Mountain Buster a further 15% — the best ally-protection buff among casters; simple to operate | **No escape skill at all** — no blink, no dash; and it must step forward for Crimson Cyclone; experienced players treat an enemy Summoner as free food if they mis-position | any | **Easy** |
| **Red Mage** 赤魔導士 | Melee-range skirmisher | **45% damage taken — excellent for a ranged job**; fights like a melee and gets away with it; Corps-a-corps + Displacement give great mobility; a near-melee combo that ignores Guard and self-barriers; Resolution is a *instant* AoE silence against a retreating group; healing on Verflare/Scorch adds sustain | Must largely complete the Enchanted Reprise combo to do its damage, which is dangerous; its AoE burst is not high enough to win a group fight outright; a jack of all trades and a master of none | Comet / Phantom Dart | Medium |
| **Pictomancer** ピクトマンサー | Universal ranged kit | **Its damage does not depend on the LB**, so rank/Battle High changes don't blunt it; Smudge is a 15m blink **plus** 25% movement speed — one of the best mobility tools in the mode; Tempera Coat barrier; instant-cast filler makes it approachable; Star Prism's zone is a genuine area denial tool if placed on the contact point | **Weak burst generation for securing KOs**, so it earns Battle High slowly; the LB has a long, exposed wind-up and is very often wasted at the back of your own group; CC needs setup; can be focused down once recognised | Comet / Phantom Dart | **Easy** |

---

<a id="part-8"></a>
## Part 8 — Map affinity matrix

One practitioner's per-map ratings for all 21 jobs (◎ excellent · 〇 good · △ situational · × poor). Map names in JP-execution order: 制圧戦 Secure, 争奪戦 Seize, 砕氷戦 Shatter, 終節戦 Naadam, 演習戦 Triumph.

| Job | Secure | Seize | Shatter | Naadam | Triumph |
|---|---|---|---|---|---|
| **Paladin** | 〇 | 〇 | ◎ | ◎ | 〇 |
| **Warrior** | ◎ | 〇 | ◎ | ◎ | ◎ |
| **Dark Knight** | ◎ | ◎ | 〇 | 〇 | ◎ |
| **Gunbreaker** | ◎ | 〇 | 〇 | 〇 | 〇 |
| **White Mage** | 〇 | ◎ | ◎ | ◎ | 〇 |
| **Scholar** | × | × | × | × | × |
| **Astrologian** | 〇 | ◎ | ◎ | ◎ | 〇 |
| **Sage** | 〇 | △ | 〇 | 〇 | 〇 |
| **Monk** | 〇 | 〇 | △ | 〇 | 〇 |
| **Dragoon** | ◎ | 〇 | ◎ | ◎ | ◎ |
| **Ninja** | 〇 | 〇 | 〇 | 〇 | ◎ |
| **Samurai** | ◎ | ◎ | 〇 | 〇 | 〇 |
| **Reaper** | ◎ | ◎ | ◎ | 〇 | ◎ |
| **Viper** | ◎ | 〇 | ◎ | 〇 | ◎ |
| **Bard** | △ | × | 〇 | 〇 | △ |
| **Machinist** | △ | △ | 〇 | 〇 | △ |
| **Dancer** | ◎ | ◎ | ◎ | ◎ | ◎ |
| **Black Mage** | 〇 | 〇 | ◎ | ◎ | ◎ |
| **Summoner** | 〇 | ◎ | 〇 | 〇 | 〇 |
| **Red Mage** | 〇 | △ | ◎ | ◎ | 〇 |
| **Pictomancer** | 〇 | 〇 | 〇 | ◎ | 〇 |

Read the matrix, not the tier list:

- **Dancer is rated top on every single map.** If you want one job that is never wrong, this is the empirical answer.
- **Shatter and Naadam reward sustained damage and objective play** (Black Mage, Red Mage, Paladin, Dragoon strong); **Secure and Seize reward burst and AoE** (Dragoon, Reaper, Dark Knight, Dancer, Samurai strong).
- **Bard is worst on the two "take and hold" maps** where it cannot set the pace, and best where fights are long lines.
- **Ninja's best map is Triumph** — the spread-field map where isolated players exist to be finished.
- **Scholar is rated poor on all five.** Reverse-engineering the cause: DoT damage cannot stop an objective being taken, and every map is decided by burst on a point.

---

<a id="part-9"></a>
## Part 9 — Job selection strategy

### The one hard rule

**Pick your job and role action before you queue, and do not change it mid-match.** Changing jobs **resets Battle High to 0**, and you can only change role actions in the spawn area. Your job choice is a commitment for 20 minutes.

### Pick by purpose, not by tier

| If you need… | Pick |
|---|---|
| **To carry a random team alone** | Viper, Dark Knight, Paladin, Dragoon (self-sufficient, high impact, defensible) |
| **To never be useless** | Dancer, Warrior, Astrologian, White Mage (forgiving, always contribute) |
| **An initiator — your team has none** | Dark Knight, Warrior, Sage, Bard, Dancer |
| **A finisher — you keep winning fights you don't convert** | Ninja, Samurai, Machinist, Dragoon |
| **To make one ally terrifying** | Bard (Bravery + Wardens Paean on the best melee), Astrologian (Astrodyne, +30% party damage), Dancer (Closed Position + the frequency of its damage) |
| **To hold an objective under fire** | Paladin, Warrior, Gunbreaker, Samurai, Monk (barriers + mitigation + self-heal) |
| **To stop an objective being taken from you** | Machinist (turret), Samurai (Chiten on the point, Return theft), Dark Knight (pull them off) |
| **A remote, low-risk contribution as a beginner** | Warrior, White Mage, Astrologian, Summoner, Pictomancer, Dancer |
| **High-skill ceiling, willing to invest** | Dark Knight, Bard, Ninja, Reaper, Machinist, Monk, Sage |

### Pick by team shape (you can only queue with 3 others)

The standard four-piece, and it still works:

**One tank/vanguard + one healer + two DPS**, with the tank forward, the healer behind, and the DPS a step behind the tank so they arrive the instant the tank commits.

Job-specific four-pieces with documented synergy:

- **Dark Knight + Reaper + Astrologian + Viper** — Dark Knight's Salt Earth is the initiation, Reaper's panic and single-target damage is the follow-up, Astrologian's Astrodyne raises both by 30%, and Viper is the standing damage. The JP analysis explicitly links Dark Knight and Reaper's value across patches.
- **Warrior + White Mage + two melee** — Warrior's CC chain plus White Mage's AoE stun and party regen is the most forgiving quartet in the game.
- **Two or more Dancers** — Contra Dance stacking is described as a legitimate and very strong composition; the counterplay is limited.
- **Bard + your best melee** — Bravery and Wardens Paean on a Viper or Dragoon is, in the source's words, "almost cheating".
- **Avoid: no healer.** Not because of healing, but because you lose the AoE stun (WHM), the 30% damage buff (AST), or the pull (SGE). Note that if the one healer is a Scholar, this is effectively a no-healer team.

### Pick by map

Use the affinity matrix in Part 8. The short version: **Dancer anywhere; Dragoon/Warrior/Reaper on the burst maps; Black Mage/Red Mage on the sustained maps; Ninja on Triumph; never Scholar.**

### Difficulty ladder (be honest with yourself)

- **Easy to get value from on match one:** Warrior, White Mage, Astrologian, Summoner, Pictomancer, Dancer.
- **Medium — needs you to know one combo and one escape:** Paladin, Gunbreaker, Dragoon, Samurai, Red Mage, Black Mage.
- **Hard — punishes imprecision, and the failure mode is feeding:** Dark Knight, Ninja, Reaper, Monk, Machinist, Sage, Bard.
- **The trap:** Bard and Summoner feel like ranged jobs you can play safely. The JP practitioner's line about Summoner is that it looks beginner-friendly but the exit from its forward dash is genuinely hard; about Bard, that it is popular with beginners and is in fact an advanced job. "There is not one ranged job that is genuinely beginner-friendly if you intend to play it properly."

### The habit that beats job choice

Because both meta lists agree that **job fit beats tier lists**, the best use of this document is:

1. Pick two jobs — one you can play without thinking (your safe pick), one you are learning.
2. Learn one role action per role properly rather than cycling through them.
3. Learn the five counter-pairs in Part 5.
4. Then stop changing jobs and start changing *positioning* — the JP analysis closes with the observation that in Frontline, **movement matters more than the job**, especially in the last five minutes.

---

<a id="part-10"></a>
## Part 10 — Tier lists, and how much to trust them

Two published views disagree, and the disagreement is instructive.

**An English PvP-service tier list (patch 7.56) ranks Frontline:**
S — Dark Knight, Dragoon, **Scholar**, Reaper.
A — Monk, Gunbreaker, Ninja, Samurai, Viper, Bard, Summoner, Red Mage, Pictomancer, Sage.

**The JP practitioner view (patch 7.5, 6,972 matches):**
Best-in-class — Paladin (burst), Dark Knight (initiation), Dancer (LB), Dragoon (AoE), Astrologian (support), Viper (all-round), Warrior (forgiving).
Weak — Scholar ("cannot move the needle"), Machinist (lacks everything Frontline wants), Monk (low Frontline suitability), Sage-as-a-healer.

**Where they collide:** Scholar. The service site puts Scholar in S-tier; the practitioner says its damage is meaningless in a mode decided by burst. Two things explain the gap: (a) a boosting site's list is partly SEO content and partly aspirational about coordinated play, where a pre-made can exploit DoT stacking; (b) the practitioner is describing a solo-queue reality where a DoT cannot stop a point being taken. **For solo queue, trust the practitioner. For a coordinated four-piece that can build around it, the service site is not absurd** — but you would be building around the least valuable role in the mode.

**A caution that both sources share:** no job in Frontline is unplayable, and the practitioner's own closing line is that working out how to excel on *every* job is the goal. Treat these rankings as a description of how much work each job needs to reach the same output — not as a list of what is allowed.

---

<a id="sources"></a>
## Sources

**Verified mechanics and role actions**

- [Role Actions (PvP) — FFXIV Online Wiki](https://ffxiv.consolegameswiki.com/wiki/Role_Actions_(PvP)) — all fifteen role actions, potencies, recasts, ranges, and the "one per role, spawn area only" rule
- [Frontline — FFXIV Online Wiki](https://ffxiv.consolegameswiki.com/wiki/Frontline) — job damage modifiers, Battle High, Limit Break charge scaling
- [Patch 7.2 notes](https://na.finalfantasyxiv.com/lodestone/topics/detail/3c4910f373e497acd3428c37f6358e341e4cc06d/) — role actions introduced

**Japanese practitioner analysis**

- [【FF14】7.5環境フロントラインジョブ考察｜FL王Mの指揮論](https://note.com/fl_king_m/n/n6c6052dad1c9) — the 7.5 per-job commander analysis; per-job damage-taken figures, burst windows, and the "Paladin is a melee / Sage is not a healer / Scholar cannot move the needle" verdicts
- [フロントラインの各ジョブ簡易解説【7.5】](https://uwasablog.com/game220803/) — three-line summary of every job, 6,972-match record disclosed in the article
- [フロントラインのタンク解説](https://uwasablog.com/game220927/) · [ヒーラー解説](https://uwasablog.com/game220928/) · [近接物理DPS解説](https://uwasablog.com/game220929/) · [遠隔物理・魔法DPS解説](https://uwasablog.com/game220930/) — per-role playbooks, per-job role-action ratings, and the per-map affinity ratings reproduced in Part 8
- [PVPロールアクション簡易解説【7.5】](https://uwasablog.com/game250510/) — the 7.5 review of all fifteen role actions, including the Bravery/Rampage "these are insane" verdicts and the Shatter ice-timing change

**English tier lists (see Part 10 for the caveats)**

- [Best FFXIV PvP Jobs 7.56 — Crystalline Conflict & Frontline](https://boostroom.com/blog/best-pvp-jobs-in-ffxiv-patch-756-crystalline-conflict-frontline-tier-list)
- [r/ffxiv — What would a Frontlines tier list look like as of the current patch?](https://www.reddit.com/r/ffxiv/comments/1ioduvi/what_would_a_frontlines_tier_list_look_like_as_of/)
