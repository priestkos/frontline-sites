---
name: ffxiv-macros
description: Use when writing or fixing FFXIV in-game macros.
version: 1.0.0
author: DalamudTranslator
license: MIT
metadata:
  hermes:
    tags: [ffxiv, macro, chat-commands, auto-translate, callouts]
    related_skills: [ffxiv-frontline, ffxiv-chat-translation]
    editorial_name: FFXIV Macro Authoring
    editorial_description: Author FFXIV in-game macros correctly — client limits, the silent failure modes, bilingual auto-translate, command reference.
---

# FFXIV Macro Authoring

Scope: `/macro` user macros for any purpose — callouts and alerts, ally-targeted actions, ground-targeted actions, crafting sequences, greetings, reports. This is the general authoring skill; `ffxiv-frontline` carries the PvP callout pack built with it.

## When to Use

- The user asks for a macro of any kind, or asks you to adapt one.
- A macro "doesn't work" / does nothing / only half-fires.
- A macro works on one client language but not another (the JP↔EN trap, below).
- Authoring bilingual or alliance-wide callouts, or report/alert macros.

## Hard limits — check these before authoring anything

| Limit | Value |
|---|---|
| Lines per macro | **15** (a 16th is discarded) |
| Characters per line | **180** |
| Blank line | **ends the macro** — everything after it is dead |
| Nested macros | **impossible** — a macro cannot call another macro |
| Conditionals / loops | **impossible** — no `if`, no repeats |
| Storage | ~100 macros per character + ~100 account-shared |
| `/wait` | integer **1–60** seconds only (`<wait.1>` ≈ 1s, no sub-second) |
| `/micon` | **only one is honoured** per macro |
| Chat throttle | **~1 message per second** — extra messages are dropped for readers |
| Action queue | **bypassed** — macro'd actions never benefit from pre-input |
| Full-width characters | **break the line** — always half-width alphanumerics and a **half-width space** |

## The eight ways a macro silently fails

Failure is quiet: an unexecutable line is **skipped and processing continues** to the next line. So a broken macro often does nothing at all with no error shown.

1. **Action names are client-language-specific.** `/ac` and `/micon` resolve names in *your client's* language. A macro written with Japanese action names stops working on an English client, and vice versa — this is the single most common cross-language failure. Fix: use the **auto-translate dictionary** for the action name (`/ac 【…】`, inserted with Tab), or Tab-complete the name so the client writes it correctly. Never copy action names out of a guide written in another language.
2. **PvP actions need `/pvpac`, not `/ac`.** `/action` does not fire PvP actions. Use `/pvpaction` (`/pvpac`). For the icon, `/micon "Name" pvpaction` — with a plain `/micon "Name"` the PvE icon is used and stays greyed out with no recast timer.
3. **A full-width character or full-width space anywhere in the line kills it.** Commands must be half-width; the separator between command and argument must be a **half-width space**. A line copied from a blog with a full-width space after `/p` will silently do nothing.
4. **A stray blank line truncates the macro.** Everything below it is dead.
5. **Starting a macro cancels the running one, and mashing a button restarts it from line 1.** Two macros cannot run concurrently. Protect a multi-line sequence with `/mlock` on/near line 1.
6. **The chat throttle eats rapid messages.** Two chat lines fired back-to-back lose the second one for readers. Join them on one line, or put `<wait.1>` between them. Mashing the button also spams duplicates — press once.
7. **`/wait` too short for the animation, or an action macro used for a rotation.** A macro'd rotation loses DPS permanently because the action queue is bypassed. Macro only: **ally-targeted single actions, ground-targeted actions, and report/alert lines.**
8. **Auto-translate hand-typed instead of Tab-inserted.** See below — a hand-typed phrase sends as plain text and does **not** translate.

## Command reference

### Chat channels — always name the channel explicitly

| Command | Scope |
|---|---|
| `/a` `/alliance` | your whole alliance (24 in Frontline / Rival Wings) — **enemies cannot see it** |
| `/p` `/party` | your 8-player party, any distance |
| `/s` `/say`, `/y` `/yell`, `/sh` `/shout` | proximity / area, **visible to enemies** |
| `/e` `/echo` | yourself only — **use this to test a macro before going live** |
| `/em` `/emote` | emote with custom text (say range) |

**Omit the channel and it goes to whatever your current chat mode is** — usually Say. That is how a private callout ends up in public chat.

### Actions

- `/ac` `/action` — `"action name" [placeholder]`. Quotes are conventional and stripped by the parser; both forms work.
- `/pvpac` `/pvpaction` — PvP actions only.
- `/pac` `/petaction` — pet actions.
- `/micon` `/macroicon` — `Name` or `Name category`. Categories seen in the wild: `pvpaction`, `emote`, `minion`, `marking`, `fieldmarking`. Macro-only command.
- `/recast` `Name` — prints the remaining cooldown as a command. Distinct from the `<recast.Name>` placeholder, which inserts the number into a chat line.

### Placeholders

`<t>` `<target>` target · `<tt>` `<t2t>` target's target · `<f>` `<focus>` focus target · `<mo>` `<mouse>` whatever is under the cursor (or the party/ally UI entry) — the best choice for healing and support macros on mouse · `<1>`–`<8>` party slot · `gtoff` ground-targeting off · `<recast.Name>` inline cooldown (e.g. `<recast.Summon Seraph>` → `1:32`) · `<se.1>`–`<se.16>` play a sound effect with the line.

### Targeting and markers

- `/ta` `/target` — target by name or placeholder (`/ta <attack1>`).
- `/targetenemy` — nearest enemy. The action-list entry **Target Attack** also auto-targets the lowest-numbered marker, which often removes the need for a targeting macro in PvP.
- `/mk` `/marking` `/enemysign` — `attack1`–`attack8`, `bind1`–`bind3`, `square`, `circle`, `cross`, `triangle` on a target. JP convention: **square = the enemy commander**, **bind markers = lock-down targets**, lowest number = the focus.
- `/fmk` `/fieldmarking` `/waymark` `/wmark` — ground markers. Subcommands `a`–`d`, `1`–`4`, `clear`, `save <1-5>`. **`/fmk D <me>` drops marker D at your feet** — repeated with `<wait.2>` it becomes a moving rally point that tracks you.

### Control

- `/wait n` `<wait.n>` — macro-only, 1–60 integer seconds.
- `/mlock` `/macrolock` — macro-only. From this line onward, no other macro may run until this one finishes.
- `/merror off` — stop "cannot use that yet" text filling the log.

## Placement

- `/mlock` and `/merror off` go **first**, before anything that can fail.
- **`/micon` placement is contested.** The EN reference says the icon line must be first to take effect; JP guides conventionally put it **last** in combat-action macros so the action is the first line executed. The one hard rule is that **only one `/micon` is honoured**. Practical rule: **text-only callout macros → `/micon` on line 1. Action macros → `/ac` first, `/micon` after.**
- Repeat an `/ac` 2–4 times to build a fallback chain, because failed lines are skipped silently.

## Bilingual macros and auto-translate (定型文)

FFXIV's auto-translate dictionary sends a phrase as a special token that each reader's client **renders in their own language** (English, Japanese, French, German). This is the only genuinely language-proof option — and the only way to reference an action name that works across client languages.

**How to insert:** in the chat box *or the macro editor*, type the first character or two, then press **Tab** (PC) or **R1/RB** (controller) and pick from the dictionary. The phrase is inserted wrapped in special coloured brackets. **Never type it by hand** — a hand-typed phrase has no token and does not translate. Pasting a token from the chat log into the macro editor also preserves it.

**Design rules for bilingual callouts:**

- **One line, both languages** — `■ RETREAT / 撤退 <se.16>` — rather than two lines, which trips the 1-message-per-second throttle.
- Prefix with `■`; JP commanders often append `卍` as a flourish.
- Reserve `<se>` for calls that must be obeyed instantly; sound on everything trains people to ignore it.
- The JP community calls firing a macro 「鳴らす」 and explicitly warns against over-ringing the alliance.

## Etiquette

- **No `<se>` on greeting macros.**
- Never place a greeting/callout macro next to a combat action on the hotbar — it gets mashed mid-rotation. Use an extended cross-hotbar page or a second palette.
- One approved chat line or two per macro; repeated presses re-run from line 1 and spam the log.

## Worked example

The complete PvP callout pack — 27 bilingual macros with sound-effect convention, hotbar layout and a JP glossary — is in the vault at
`sources/03-callout-macros.md`.
Use it as the template for any callout set.

## Pre-flight checklist

1. Half-width only; half-width space after every command.
2. No blank lines inside the macro.
3. `/mlock`, `/merror off` near the top if the macro is multi-line or can be mashed.
4. Channel named explicitly on every chat line.
5. Action names match **the client language this macro will run on** (or are auto-translate tokens).
6. `/pvpac` for PvP actions, `/micon … pvpaction` for their icons.
7. `/wait` long enough for the animation.
8. Chat lines that must both be seen are joined into one line, or separated by `<wait.1>`.
9. Test with `/e` before going live, and press the button **once**.

## Sources

- [FFXIV Online Wiki — Macro](https://ffxiv.consolegameswiki.com/wiki/Macro) (command table, placeholders, `<recast.X>`, alliance chat)
- [FFXIV Online Wiki — Auto-Translate](https://ffxiv.consolegameswiki.com/wiki/Auto-Translate)
- [Macrology (3rd edition)](https://github.com/FFXIVMacrology/Macrology/blob/main/%5Ben%5DMacrology(the%20Third%20Edition).md) (15-line/180-char limits, throttle, `/pvpac`)
- [Lodestone — /pvpaction](https://eu.finalfantasyxiv.com/lodestone/playguide/db/text_command/195d3255bd3/)
- [エオリーマン — マクロが正しく動かない時に確認すべきこと](https://eoryman.com/2019/11/30/macro-error/) (silent line skips, overwrite, `/mlock`)
- [エオリーマン — マクロの教科書](https://eoryman.com/2020/05/11/macro-beginner/)
- [FF14の井戸端 — マクロのアレコレ](https://ff14-idobata.blog.jp/archives/5667344.html) (no nesting/loops, `/micon` placement convention)
- [はてなブログ — マクロについて](https://irischang.hateblo.jp/entry/2024/03/16/140436) and [コトリログ — 言語設定](https://kotorilog.com/ff14/language-settings/) (action names are client-language-specific; the auto-translate fix)
- [FF14定型文マクロの正しい作り方](https://stage-intranet.joshsoftware.com/akiruno-bara/9044596/) (Tab-insert requirement, no action queue)
- [テキストコマンド一覧](http://ff14.ffo.jp/html/28.html) (macro-only command markers)
