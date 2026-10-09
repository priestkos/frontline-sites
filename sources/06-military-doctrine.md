# Military doctrine applied to FFXIV Frontline

Derivations, citations and reasoning behind the 14 named plays. Companion to SKILL.md.

---

## 1. The nine principles of war (MOOSEMUSS)

**Mass, Objective, Offensive, Security, Economy of force, Manoeuvre, Unity of command, Surprise, Simplicity.** The principles are linked through the master principle, the objective.

| Principle (doctrinal wording) | Frontline translation | Failure it names |
|---|---|---|
| Objective — direct every operation toward a clearly defined, decisive, attainable objective | The win condition is a rating threshold, not kills | Farming kills off the objective |
| Offensive — seize, retain and exploit the initiative | Whoever decides where the next fight happens wins | Reacting to enemy triangles all match |
| Mass — concentrate combat power at the decisive place and time | One 20-man body, not three 8s | The 8/8/8 split |
| Economy of Force — minimum essential to secondary efforts | Two scouts, one reserve | Sending 12 to a fringe node |
| Manoeuvre — place the enemy at a disadvantage by flexible application | Terrain plus arrival timing | Taking the fight they chose |
| Unity of Command — unity of effort under one responsible commander | One caller | Six competing plans |
| Security — never permit an unexpected advantage | Reserve plus flank watch | Getting pinched |
| Surprise — strike where he is unprepared | Rear-ring nodes, off-timer pushes | Marching into the contested centre |
| Simplicity — clear plans, concise orders | "REGROUP SOUTH" | The three-part plan nobody reads |

Sources: [DTIC, A Model to Study Modern War](https://apps.dtic.mil/sti/tr/pdf/ADA503932.pdf) · [Oxford Academic, What is military strategy?](https://academic.oup.com/book/57480/chapter/466865884)

---

## 2. Lanchester's square law

With aimed fire where each unit can shoot at any target and receive fire from any direction, **combat power ∝ n²**, not n.

- 2 vs 3 → advantage 3² − 2² = 5
- 2 vs 4 → 4² − 2² = 12
- 2 vs 5 → 5² − 2² = 21
- A 2:1 numerical edge = **4× firepower**; a 3:1 edge = **9× combat power**.
- Group fighting ability rises with the **square** of group size but only **linearly** with individual fighting ability — defeating a force three times as numerous requires fighters **nine times** as effective.

Frontline is square-law warfare because AoE damage lets every player hit every target in a blob. This is why the death ball wins and why an individually skilled player cannot carry.

**Where the law breaks:** Lanchester's own model set — *concentrated fire favours a square-law outcome, whereas positional fire and one-to-one combat favour a linear-law outcome.* Corridors, corners, ramps and LoS-breaking terrain convert an n² fight into an n¹ fight. Hence **The Defile**, and hence never pursuing a routed enemy into a bottleneck.

**Inversion for the attacker:** splitting an enemy 24 into 12 + 12 destroys half their combat power without a kill. Frontline's multiple simultaneous objectives are the mechanism to force that split — **objectives are a dispersion machine**, not merely income.

**7.5 amendment:** Battle High no longer drops on death, so dying costs tempo (respawn travel) and rating (Secure −10; Shatter +8 to the enemy), not your power curve. Post-7.5 doctrine shifts from *preserve Battle High above all* to **preserve bodies and position**, and makes deliberate aggressive trades at objectives more defensible.

Sources: [Lanchester's laws](https://en.wikipedia.org/wiki/Lanchester%27s_laws) · [Force concentration](https://en.wikipedia.org/wiki/Force_concentration) · [Lanchester's laws for game design](https://www.gamedeveloper.com/design/the-designer-s-notebook-kicking-butt-by-the-numbers-lanchester-s-laws)

---

## 3. Concentration, the reserve, interior lines

**Schwerpunkt / centre of gravity.** Clausewitz: "the hub of all power and movement, on which everything depends… the point against which all our energies should be directed." Name one decisive point per phase and mass on it.

**The decisive reserve.** Economy of force allocates minimum essential power to secondary efforts, accepting risk in selected areas to achieve overwhelming effect in decisive operations. In Frontline that reserve has three jobs:

1. **Security** — the third team *will* arrive at every fight the other two can see.
2. **Exploitation** — Liddell Hart: *"You cannot hit the enemy with effect unless you have first created the opportunity; you cannot make that effect decisive unless you exploit the second opportunity that comes before he can recover."*
3. **Counter-punch** — the only moment six players beat ten is while the ten are committed to your main body.

**Interior lines (Jomini).** "…those adopted by one or two armies to oppose several hostile bodies, and having such a direction that the general can concentrate the masses and maneuver with his whole force in a shorter period of time than it would require for the enemy to oppose to them a greater force." Interior lines let a numerically inferior force achieve local superiority; exterior lines divide you into fractions the enemy crushes successively.

Frontline pivots: **Secure** mid-ring + pillar · **Triumph** central gully (also the ranged high ground) · **Onsal** the centre, where S-rank ovoos spawn.

Sources: [Clausewitz: fog, friction, centre of gravity, culminating point](https://www.globalsecurity.org/military/library/report/1991/HHT.htm) · [Interior lines](https://en.wikipedia.org/wiki/Interior_lines) · [FMFRP 12-13, Maneuver in War](https://www.marines.mil/Portals/1/Publications/FMFRP%2012-13%20%20Maneuver%20in%20War.pdf)

---

## 4. The indirect approach and deception

Liddell Hart: **"Dislocation is the aim of strategy; its sequel may be either the enemy's dissolution or his easier disruption in battle."** His study of 280 campaigns in 25 centuries found only **six** occasions where a decisive result followed a *direct* strategic approach to the enemy's main army. Aim for the **line of least expectation** and the **line of least resistance**.

Sun Tzu: **"All warfare is based on deception. Hence, when able to attack, we must seem unable; when using our forces, we must seem inactive; when we are near, we must make the enemy believe we are far away; when far away, we must make him believe we are near."** The *cheng* (direct/fixing) force distracts; the *ch'i* (extraordinary/indirect) force strikes where the blow is not anticipated.

**Frontline's mechanical gift:** the enemy map shows only players within sight range of their own units. The enemy's entire sensor picture is therefore spoofable — tight visible columns read as larger forces, hidden main bodies read as smaller. Almost nobody exploits this.

Sources: [Liddell Hart, Strategy (1954)](https://classicsofstrategy.com/2016/01/19/liddell-hart-strategy-1954/) · [The Indirect Approach — Strategy: A History](https://erenow.org/ww/strategy-a-history/12.php) · [The Art of War, ch. I and VI](https://classics.mit.edu/Tzu/artwar.html)

---

## 5. Time: Boyd's OODA loop

Boyd: operate **inside** the adversary's observe–orient–decide–act cycle — "change the situation more rapidly than the opponent can comprehend," forcing him to *re*-observe, *re*-orient, *re*-decide, *re*-act. Getting inside his time cycle **inflicts disorder on him**. The point is not raw speed but making his orientation fail.

**Frontline timers are public**, which is unusual and exploitable: Shatter small ice at 12:30 and 4:30; Triumph snow ~16:00 and auroras ~9:00; Secure teleport pads live 30s before the weaponry spawn. Pre-declare the rotation and be on the objective before it becomes an objective.

**Sunk-cost strike:** attack exactly when a team has committed to an objective. Their options become "forfeit what we've paid for" or "stay and eat the fight" — a choice between two losses is the ideal attack.

Source: [Let Boyd Speak! — OODA and maneuver warfare (Marine Corps Association)](https://www.mca-marines.org/wp-content/uploads/Let-Boyd-Speak.pdf)

---

## 6. The culminating point

Clausewitz: the attacker's superiority **diminishes as the attack advances** until the **culminating point of the attack**, at which "the superior strength of the attack… is just enough to maintain a defense and wait for peace." Beyond it "the scale turns and the reaction follows with a force that is usually much stronger than that of the original attacker."

Frontline translation: **do not pursue to the landing platform.** Respawns emerge there with 10 seconds of Invincibility; a pursuing, wounded, cooldown-less force is exactly the "stronger reaction" Clausewitz describes. Stop at the objective line, remount, redeploy.

**Corollary — never reinforce failure** (Liddell Hart: reinforce success, not failure). Committing more bodies to a losing fight feeds the enemy Battle High and rating. Trickling in is the enemy defeating you in detail.

Source: [Clausewitz, via GlobalSecurity](https://www.globalsecurity.org/military/library/report/1991/HHT.htm)

---

## 7. Coalition dynamics in a three-way game

Game theory and history agree that **at each stage the weakest players align against the strongest** — alliances form to restore the balance of power. There is also a documented **paradox of power**: a player can suffer from being too strong, because a runaway leader becomes everyone's target and finds it hard to partner with weaker players.

Applied:

- **1st place** — Quiet Leader: accumulate, stay unc lumped, avoid the centre. Your enemy is the clock. A visible runaway leader converts a won game into a 2-v-1.
- **2nd place** — attack the leader's *rate*, not their existence. Annihilating 1st for free simply crowns 3rd; keep the third team alive as a distraction.
- **3rd place** — you need chaos. Your enemy is the stalemate. Create and prolong fights between the other two, then sweep objectives while they grind.

Sources: [Endogenous formation of alliances in conflicts](https://sites.socsci.uci.edu/~mrgarfin/OUP/papers/Bloch.pdf) · [Too Big to Prevail: The Paradox of Power in Coalition Formation](https://www.ifo.de/DocDL/cesifo1_wp8980.pdf)

---

## 8. Play-to-doctrine index

| Play | Doctrine | Mechanic it exploits |
|---|---|---|
| The 4× Rule | Lanchester square law | AoE = every player can hit every target |
| The Defile | Lanchester linear law | LoS-breaking terrain and chokes |
| The Split Forcing | Lanchester inverted | Multiple simultaneous objectives |
| The Schwerpunkt | Clausewitz centre of gravity | The map's single highest-value objective |
| The Floating Squad | Economy of force / security | The guaranteed third-party pinch |
| The Pivot | Jomini interior lines | Central map positions and mount travel time |
| Trade the Centre for the Ring | Indirect approach | Mid-tier objectives left alone during the S-rank stalemate |
| The Rear-Ring Raid | Lines of retreat | Under-defended nodes near enemy bases |
| The Anvil and the Hammer | Sun Tzu cheng/ch'i | Enemy squads detached by objective threats |
| The Ghost Flank | Sun Tzu deception | Sight-range-only enemy display on the map |
| The Pre-Load | Boyd OODA | Public spawn timers |
| The Sunk-Cost Strike | Boyd, breaking the loop | Enemies mid-channel or mid-objective |
| Break Contact on Victory | Culminating point | 10s spawn Invincibility |
| The Quiet Leader | Coalition dynamics | Two enemies who would rather fight each other |
