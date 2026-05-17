# Relevant clockworkpi.com forum threads

> Useful threads from <https://forum.clockworkpi.com/c/picocalc/> for context, gotchas, and community knowledge. Captured 2026-05-17.

The forum is the active community channel for PicoCalc + MMBasic. Geoff Graham (PicoMite author) and Peter Mather post here, as does Michael Adcock (madcock — RC firmware maintainer).

## Programming on the PicoCalc

<https://forum.clockworkpi.com/t/programming-on-the-picocalc/16670> — entry-level Q&A. Common confusions:

- "How do I force PRINT output to next line?" — by default `PRINT` already adds CRLF; trailing `;` *suppresses* the newline.
- Long program lines and how to split them (use `OPTION CONTINUATION LINES ON` + ` _` at end of line).
- `SQR(a*a + b*b)` — must assign or print: `y = SQR(...)` or `PRINT SQR(...)`. Naked function calls on a line give "Unknown command".

## New MMBasic manual 18 July 25

<https://forum.clockworkpi.com/t/new-mmbasic-manual-18-july-25/18695> — announcement of the latest manual revision (still the "Revision 1, 18 July 2025" PDF, ~2.6 MB).

A user notes one error still in that revision: `PLAY TONE` syntax on page 143 says

```
PLAY TONE left [, right [, dur] [,interrupt]]]
```

but the correct form requires *both* left and right frequencies:

```
PLAY TONE left, right [,dur] [,interrupt]
```

(Useful for lesson 06 — Sound and time.)

## MMBasic Style Guide for GPT

<https://forum.clockworkpi.com/t/mmbasic-style-guide-for-gpt/18271> — Lennart Hennigs' announcement of his style guide, written so an LLM can produce idiomatic MMBasic code instead of generic BASIC.

The style guide itself lives in `LennartHennigs/PicoCalc-Notes` repository as `src/CLAUDE.md` (renamed from `mmbasic_style.md` in September 2025). Mirrored in this repo as `references/community/mmbasic_style_guide.md`.

## Collecting MMBasic code examples for PicoCalc

<https://forum.clockworkpi.com/t/collecting-mmbasic-code-examples-for-picocalc/17984> — adcockm started a thread that grew into the TiddlyWiki at `michaeladcock.info/temp/PicoCalc_MMBasic.html`.

## Documentation of graphics functions on PicoCalc basic?

<https://forum.clockworkpi.com/t/documentation-of-graphics-functions-on-picocalc-basic/18495> — direct reference to the official manual's graphics chapter is the canonical source. Mirrored at `references/manual/PicoMite_User_Manual.pdf`.

## Building MMBasic from source

<https://forum.clockworkpi.com/t/building-mmbasic-from-source/19836> — for the brave: how to compile your own PicoMite firmware variant (RP2040 / RP2350) with custom config.

## ChatGPT Program Creation

<https://forum.clockworkpi.com/t/chatgpt-program-creation/19606> — discussion of LLMs generating MMBasic code. Reinforces the value of the style guide as a system prompt.
