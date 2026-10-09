# FFXIV Frontline — Bilingual Callout Macro Pack (EN / JP)

Every macro fires **English + Japanese on the same line**, so it reads instantly for both a JP reader and an EN reader. Channel is `/a` (alliance) — in Frontline your 24-player team *is* an alliance of three parties, so `/a` reaches all 23 teammates regardless of distance. **Enemies cannot see alliance chat.**

Companion to `ffxiv-frontline-complete-guide.md`. Patch 7.5 era.

---

## 0. Install

1. **System menu → User Macros** (or type `/macro`).
2. Pick a free slot → name it → paste the lines into the big text box.
3. **Line 1 must be `/micon …`,** otherwise the icon line is ignored. (Also optional — skip it and the macro uses a plain icon.)
4. Right-click the macro → **Register to Hotbar**, then place it on a hotbar or the cross hotbar.
5. `/micon` takes an action name. For callout macros the cleanest choices are marker icons:
   - `/micon attack1 marking` — the "1" attack-marker icon, ideal for BURST calls
   - `/micon square marking` — the square icon, ideal for COMMAND calls
   - `/micon A fieldmarking` — an A-marker icon, ideal for the rally-point macro
   - or just any action name you recognise, e.g. `/micon "Sprint"`

---

## 1. Technical rules you must respect

These are the real client limits — break them and calls silently fail.

| Rule | Value | Why it matters |
|---|---|---|
| Lines per macro | **15 max** | A 16th line is discarded |
| Characters per line | **180 max** | Keep bilingual lines short |
| Chat throttle | **~1 message per second** | Two `/a` lines fired back-to-back → **the second is dropped for readers**. Separate them with `<wait.1>` |
| `/wait` | integer 1–60 (seconds) | `<wait.1>` ≈ 1 second |
| `/micon` | first line only, once | Later occurrences are ignored |
| `<se.1>`–`<se.16>` | sound effect with the message | The single most important element — see §3 |
| `/mlock` | locks the macro | Prevents another macro interrupting a multi-line sequence. Use it on the burst countdown |
| `/merror off` | suppresses error text | Stops "not in range" spam filling your log |
| Blank line | **ends the macro** | Never leave a blank line mid-macro |
| A line not starting with `/` | sent as chat text | Handy, but always use the `/a` form explicitly |

**Do not** put two `/a` messages on consecutive lines. Either join them on one line with ` / `, or put `<wait.1>` between them.

---

## 2. Design rules

- **One line, two languages.** `■ RETREAT / 撤退 <se.16>` costs one line, no throttle risk, readable to everyone at a glance.
- **`■` bullet prefix.** Universal in JP Frontline callouts — it makes your message stand out in a scrolling log.
- **`卍` optional flourish.** JP commanders often append 卍 (manji) as a stylistic marker. It reads as native JP front-line culture and is harmless. Add it if you want to look like a JP commander; drop it if you want to look neutral. Nothing about it is offensive or religious in this context.
- **Boundary markers in ALL CAPS.** `【RETREAT】` / `【撤退】` so it's distinguishable at a glance mid-fight.
- **Sound only on the calls that must be obeyed instantly.** Every call with `<se>` is an interrupt to 23 people. The JP community calls firing a macro 「鳴らす」 ("ringing it") and warns against spamming — over-ringing your alliance is the fastest way to be ignored.
- **Arrows for direction:** `→→東→→` etc. is the JP convention and is language-neutral. Keep it.
- **Never two callouts at once.** One voice, one instruction (unity of command).

---

## 3. The sound-effect convention

Use the same mapping the JP commander community uses, so your calls *sound* familiar to JP players even before they read them.

| SE | Meaning | Typical use |
|---|---|---|
| `<se.1>` | neutral attention | movement / direction calls |
| `<se.2>` | light attention | target identification (which GC, which objective) |
| `<se.3>` | countdown tick | burst countdown 3 / 2 / 1 |
| `<se.4>` | "get ready" | burst prep |
| `<se.5>` | caution | reposition, they're bursting first |
| `<se.6>` | decisive | burst now, turn around and fight |
| `<se.7>` | instruction | objective priority, base recall, climb/descend |
| `<se.9>` | alarm | pincer incoming |
| `<se.10>` | contact | follow me, marker up |
| `<se.13>` | standby | hold / wait |
| `<se.16>` | emergency | **retreat**, correction, hard abort |

---

## 4. The macro set

### Group A — Rally & positioning

**M01 — RALLY: follow the D marker (moving waypoint)**
```
/micon A fieldmarking
/a ■ FOLLOW ME / 集合・追従 <se.10>
/fmk D <me><wait.1>
/fmk D <me><wait.2>
/fmk D <me><wait.2>
/fmk D <me><wait.2>
```
*JP: 集合・追従 — shūgō / tsujū — "gather / follow".*
Places **field marker D at your feet** and refreshes it four times over ~7 seconds, so a moving rally point tracks you. `/fmk` is `/fieldmarking`; `/fmk D <me>` drops marker D on your character. This is the JP commander's standard "follow me" macro.

**M02 — REGROUP (static)**
```
/micon square marking
/a ■【REGROUP】/【集合】<se.1>
```
*JP: 集合 — shūgō.*

**M03 — CENTRE**
```
/a ■ 卍 CENTRE 卍 / 中央 <se.1>
```
*JP: 中央 — chūō.*

**M04 — DIRECTIONS (four macros)**
```
/a ■→→ EAST →→ / 東 <se.1>
/a ■←← WEST ←← / 西 <se.1>
/a ■↓↓ SOUTH ↓↓ / 南 <se.1>
/a ■↑↑ NORTH ↑↑ / 北 <se.1>
```
*JP: 東 higashi / 西 nishi / 南 minami / 北 kita.* Arrows are language-neutral; keep them.

**M05 — CLIMB / DESCEND THE CLIFF (Shatter, Onsal)**
```
/a ■↑【CLIFF】UP / 崖を登ります <se.7>
/a ■↓【CLIFF】DOWN / 崖を降ります <se.7>
```
*JP: 崖 — gake — "cliff".* Warns the mass before you commit it to a drop with no retreat.

**M06 — HOLD / WAIT**
```
/a ■【HOLD】/【待機】<se.13>
```
*JP: 待機 — taiki — "stand by".*

**M07 — SPREAD / TAKE THE FIELDS (Triumph, Onsal)**
```
/a ■【SPREAD - TAKE FIELDS】/【分散・フィールド確保】<se.7>
```
*JP: 分散 — bunsan — "disperse / spread out".*

### Group B — Engage & burst

**M08 — BURST PREP (marker 1)**
```
/micon attack1 marking
/a ■【MARKER 1】BURST PREP /【1タゲ付近】バースト準備 <se.4>
```
*JP: 1タゲ付近 — wan-tage fukin — "near target marker 1"; バースト準備 — bāsuto junbi — "burst preparation".*

**M09 — BURST COUNTDOWN (the one multi-line macro worth having)**
```
/merror off
/mlock
/a ■ COUNTDOWN / カウントダウン開始 <se.1><wait.1>
/a ■ 3 <se.3><wait.1>
/a ■ 2 <se.3><wait.1>
/a ■ 1 <se.3><wait.1>
/a ■【BURST NOW】/【突撃】<se.6>
```
*JP: カウントダウン — kauntodaun; 突撃 — totsugeki — "charge".* `/mlock` stops another macro interrupting the sequence. The `<wait.1>` between lines defeats the 1-message-per-second throttle. 8 lines — well inside the 15-line limit.

**M10 — PUSH / GO**
```
/a ■【PUSH】/【押し上げ】<se.6>
```
*JP: 押し上げ — oshi-age — "push up".* (JP players also use 「凸」/to read as a charge-in slang; keep 押し上げ for a command.)

**M11 — FOCUS THIS TARGET**
```
/merror off
/a ■【FOCUS - KILL THIS】/【これ集中・落とす】<se.10>
/mk attack1 <t><wait.1>
/mk attack1 <t>
```
*JP: これ集中 — kore shūchū — "focus this"; 落とす — otosu — "take them down".* Places marker 1 on your current target twice (the second application sticks after any instant cleanse).

**M12 — TURN AROUND AND FIGHT (they're bursting into us)**
```
/a ■ THEY BURST FIRST - DODGE / 先にバースト来ます・回避 <se.5>
/a ■ TURN & FIGHT / 反転して迎撃 <se.6>
```
*JP: 先にバースト — saki ni bāsuto — "they burst first"; 回避 — kaihi — "evade"; 反転 — hanten — "turn around".* Note the `<wait.1>` implied by using two lines — the throttle drops rapid doubles, so if you want both lines guaranteed, insert `<wait.1>` at the end of line 1.

**M13 — ATTACK THE LEADING GRAND COMPANY (three variants)**
```
/a ■ ATTACK THE LEADER / 1位を攻撃 <se.2>
/a ■ TARGET: MAELSTROM【RED】 / 黒渦団【赤】 <se.2>
/a ■ TARGET: TWIN ADDER【YELLOW】 / 双蛇党【黄】 <se.2>
/a ■ TARGET: FLAMES【BLUE】 / 不滅隊【青】 <se.2>
```
*JP: 黒渦団 kuro-udan (Maelstrom, red) / 双蛇党 sōjadan (Twin Adder, yellow) / 不滅隊 fumetsutai (Immortal Flames, blue).* Use these when your team is fighting the wrong team while the leader takes the win.

### Group C — Withdraw & safety

**M14 — PINCER WARNING**
```
/a ■【PINCER INCOMING】/【挟撃注意】<se.9>
```
*JP: 挟撃注意 — kyōgeki chūi — "beware of a pincer".* Fire this the moment you see triangles closing from a third direction. Usually paired with M15.

**M15 — RETREAT**
```
/a ■【RETREAT】/【撤退】<se.16>
```
*JP: 撤退 — tettai.*

**M16 — FALL BACK A LITTLE (not a full retreat)**
```
/a ■【PULL BACK A BIT】/【少し下がって】<se.5>
```
*JP: 少し下がって — sukoshi sagatte — "back off a little".*

**M17 — RECALL TO BASE (use Return)**
```
/a ■【TO BASE - USE RETURN】/【自陣OPまで・デジョン】<se.7>
```
*JP: 自陣OP — jijin OP — "own base / home OP"; デジョン — dejon — the JP nickname for Return.* Recalling resets your position and lets you rebuild; the base is a safe zone. **Note it also resets Battle High if you swap jobs — recall to regroup, not to job-swap.**

**M18 — NO DEEP CHASE**
```
/a ■【NO CHASE】/【深追い注意】<se.5>
```
*JP: 深追い注意 — fukaoi chūi — "beware of over-pursuing".* Fire this the instant the fight is won. It is the single highest-value macro in the pack because pursuit is where matches get thrown.

**M19 — PLAY SAFE / DON'T DIE**
```
/a ■【PLAY SAFE - DON'T DIE】/【いのちだいじに】<se.7>
```
*JP: いのちだいじに — inochi daiji ni — literally "take good care of your life", a JP gaming idiom for "play defensively".* Fire when you already have the score to win.

**M20 — REGROUP AFTER A WIPE (anti-trickle)**
```
/a ■【REGROUP - NO TRICKLE】/【立て直し・バラバラ禁止】<se.1>
```
*JP: 立て直し — tate-naoshi — "rebuild / re-form"; バラバラ禁止 — barabara kinshi — "no going in piecemeal".* This is the call that stops your team being defeated in detail.

**M21 — CORRECTION**
```
/a ■【CORRECTION - IGNORE LAST】/【訂正します】<se.16>
```
*JP: 訂正します — teisei shimasu — "I'm correcting that".* Always correct a bad call loudly rather than letting 20 people walk into it.

### Group D — Objectives

**M22 — SECURE AND DEFEND OBJECTIVES**
```
/a ■【SECURE & DEFEND】/【拠点を確保・防衛】<se.7>
```
*JP: 拠点 — kyoten — "stronghold/objective"; 確保 kakuho "secure", 防衛 bōei "defend".* On Seize, JP players usually call tomeliths **リス** (*risu*, from アラガントームリス). If your group is JP-heavy you can use 「リス確保・防衛」 instead.

**M23 — ICE PRIORITY (Shatter)**
```
/a ■【BIG ICE FIRST】/【大氷優先】<se.2>
/a ■【SMALL ICE FIRST】/【小氷優先】<se.2>
```
*JP: 大氷 — dai-kōri — "large ice"; 小氷 — shō-kōri — "small ice".*

**M24 — THE SPLIT CALL (main body / light party)**
```
/a ------------
/a ■ MAIN BODY / 本体は
/a ■ LIGHT PARTY / 少人数ライトパーティは
```
*JP: 本体 — hontai — "the main body"; 少人数ライトパーティ — shō-ninzū raito pātī — "the small light party".* Fire this followed by M03/M04/M22 to task each element separately. This is how you threaten three objectives at once without splitting your mass evenly.

### Group E — Utility

**M25 — TARGET MARKER 1 (no chat spam)**
```
/merror off
/ta <attack1>
```
Targets whatever bears marker 1. Most bursts are called on marker 1; some groups use the circle marker (`/ta <circle>`). Recently added to the action list: **Target Attack**, which automatically targets the lowest-numbered marker — if you have it on your bars you may not need this macro at all.

**M26 — MARK THE PRIORITY TARGET (square = the enemy commander)**
```
/merror off
/mk square <t>
/mk bind1 <t>
```
*JP convention: 四角 (square) marks the enemy commander; 足止め (bind markers) mark whoever must be locked down.* Community practice is to use the lowest number available so everyone knows the focus.

**M27 — LIGHT PARTY REPORT (LB / action ready)**
```
/a ■ LB READY / LB準備完了 <se.7>
```
*JP: 準備完了 — junbi kanryō — "preparation complete".* Keep these rare — they are the most commonly spammed and most commonly resented macros in the mode.

---

## 5. Hotbar layout

Two rows of eight covers the core set on keyboard or cross-hotbar. **Row 1 = react, Row 2 = direct.**

| Slot | Row 1 — react to the enemy | Row 2 — direct your team |
|---|---|---|
| 1 | M14 PINCER | M01 RALLY |
| 2 | M15 RETREAT | M02 REGROUP |
| 3 | M16 PULL BACK | M08 BURST PREP |
| 4 | M18 NO CHASE | M09 COUNTDOWN |
| 5 | M19 PLAY SAFE | M10 PUSH |
| 6 | M17 TO BASE | M22 SECURE & DEFEND |
| 7 | M20 NO TRICKLE | M03 CENTRE |
| 8 | M21 CORRECTION | M07 SPREAD / M24 SPLIT |

The three you will press most: **M01 (rally), M15 (retreat), M18 (no chase).**

**Minimal starter set if you only want six macros:** M01 rally · M08 burst prep · M09 countdown · M14 pincer · M15 retreat · M18 no chase.

---

## 6. Auto-translate (定型文) — the language-proof option

FFXIV has a built-in **auto-translate dictionary**: certain phrases are sent as special tokens and are **displayed in each reader's own client language** (the dictionary supports English, Japanese, French and German). A phrase you insert as a token will appear as Japanese in a JP client and English in an EN client — no bilingual line needed.

**How to insert one:**
1. In the **macro editor** text box, type the first character or two of the JP phrase (e.g. `しゅう` for 集合).
2. Press **Tab** (PC) or **R1/RB** (controller) to open the dictionary and pick the phrase.
3. The phrase is inserted wrapped in the special green/red tokens. **Do not type it by hand** — a hand-typed phrase sends as plain text and does **not** translate.

Phrases that exist in the dictionary and are useful in Frontline (JP → what a JP client shows):

| JP phrase | Romaji | Meaning | EN client shows |
|---|---|---|---|
| 双蛇党 | sōjadan | Twin Adder | Twin Adder |
| 黒渦団 | kuro-udan | Maelstrom | Maelstrom |
| 不滅隊 | fumetsutai | Immortal Flames | Immortal Flames |
| 東 / 西 / 南 / 北 | higashi / nishi / minami / kita | East / West / South / North | East / West / South / North |
| 中央 | chūō | centre | Centre |
| 集合 | shūgō | gather | Gather |
| 追従 | tsujū | follow | Follow |
| デジョン | dejon | Return | Return |
| 使ってください。 | tsukatte kudasai | please use (it) | Please use it. |
| 少し下がって。 | sukoshi sagatte | back off a little | Move back a little. |
| 待機します。 | taiki shimasu | standing by | Standing by. |
| バースト | bāsuto | burst | Burst |
| 回避してください！ | kaihi shite kudasai | please evade | Please avoid it! |
| ライトパーティ | raito pātī | light party | Light Party |

**Trade-off:** dictionary phrases are language-proof but slow to insert and limited in vocabulary. `■` bullets, `卍`, arrows and the ALL-CAPS `【…】` form are **not** dictionary entries — you get those only by typing them literally, which is why every macro in §4 carries an explicit EN + JP line instead. Use both: dictionary tokens where a phrase exists and speed isn't critical, literal bilingual lines for fast tactical calls.

---

## 7. JP Frontline glossary (for reading what comes back)

| JP | Romaji | Meaning |
|---|---|---|
| フロントライン | furonto-rain | Frontline |
| アライアンス | araiansu | alliance (your 24-player team) |
| ライトパーティ | raito pātī | light party (an 8-player party inside the alliance) |
| 自陣OP | jijin OP | your own base / home OP |
| デジョン | dejon | Return (the spell) |
| 鳴らす | narasu | "to ring it" — fire a callout macro |
| 軍師 | gunshi | strategist / the shot-caller |
| 床ペロ | yuka-pero | dying ("floor-licking") |
| 凸る | totsuru | to charge in (from 突撃) |
| 芋る | imoru | to sit back and play passively (usually derogatory) |
| リス | risu | tomelith (from アラガントームリス) |
| 大氷 / 小氷 | dai-kōri / shō-kōri | large ice / small ice (Shatter) |
| オボー | obō | ovoo (Danshig Naadam) |
| 挟撃 | kyōgeki | pincer / flanking attack |
| 撤退 | tettai | retreat |
| 深追い | fukaoi | over-pursuing |
| 立て直し | tate-naoshi | re-forming / regrouping |
| バースト | bāsuto | burst (focused fire) |
| タゲ | tage | target (from ターゲット) |
| カウントダウン | kauntodaun | countdown |
| 反転 | hanten | turning around |
| 訂正 | teisei | correction |
| いのちだいじに | inochi daiji ni | play safe / protect your life |
| 地図 | chizu | the map (watch it) |

---

## 8. Sources

- [うわさの調べ — フロントライン指揮マクロ紹介【PvP】](https://uwasablog.com/game250831/) (the JP commander macro set this pack is modelled on: `/a`, `/mlock`, `/fmk D <me>`, SE conventions, the 卍 flourish, the 定型文 list)
- [うわさの調べ — フロントラインで使えるマクロ紹介【PvP】](https://uwasablog.com/game230207/) (marker targeting, `/targetenemy`, focus-target macros, alliance report macros and the anti-spam etiquette)
- [FFXIV Online Wiki — Macro](https://ffxiv.consolegameswiki.com/wiki/Macro) (15-line limit, `/alliance`)
- [FFXIV Online Wiki — Auto-Translate](https://ffxiv.consolegameswiki.com/wiki/Auto-Translate)
- [Macrology — macro line and character limits, the 1-message-per-second throttle](https://github.com/FFXIVMacrology/Macrology/blob/main/%5Ben%5DMacrology(the%20Third%20Edition).md)
- [FF14 Online Wiki — テキストコマンド](https://ff14wiki.info/?%E3%83%86%E3%82%AD%E3%82%B9%E3%83%88%E3%82%B3%E3%83%9E%E3%83%B3%E3%83%89) (`/fmk` = `/fieldmarking`; `/micon` icon syntax)
- [JP Lodestone — フロントライン](https://jp.finalfantasyxiv.com/lodestone/playguide/contentsguide/frontline/) (official JP names: ウォーコー・チーテ（演習戦）etc.)
