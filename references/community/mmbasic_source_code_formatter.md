# MMBasic Source Code Formatter (Hugh Buckle / Geoff Graham)

> Source: <https://fruitoftheshed.com/wiki/doku.php?id=mmbasic_original%3Ammbasic_source_code_formatter>
> "Fruit of the Shed" community wiki. Module dated 20 April 2013 (`Format.bas` v2.3). Fetched 2026-05-17.
>
> The wiki itself notes: *may reference functionality which has changed or is deprecated in the latest versions of MMBasic.* So treat it as a historical canon, not strict guidance for RC23. Still useful — the indenting rules below are how the language idiomatically formats itself.

---

## Format.bas — what it does

A self-hosted formatter (MMBasic program) that re-indents source code to highlight program structure. Default indent is 2 spaces per level. It does not change tokens — only leading whitespace.

Invocation forms (1 = primary):

```basic
RUN "FORMAT.BAS"                                ' interactive prompts
FORMAT InFileName[.bas] OutFileName[.bas] [Indent] [/P]   ' implied-run command line
CHAIN "FORMAT.BAS"                              ' from another program (with CMDParm$ or FORMAT.DAT)
```

`/P` lists output to screen pausing each screenful.

## The standard set of rules (canonical MMBasic formatting)

1. Lines starting with a **label** are aligned to the left margin — as are `SUB`, `END SUB`, `FUNCTION`, `END FUNCTION`.
2. The first non-label line is indented to the first level.
3. Lines following a single-line `IF`, `DO` or `FOR` are not further indented.
4. Multiline `DO` and `FOR` have their respective `LOOP` and `NEXT` aligned. Intervening lines are indented one level.
5. The `NEXT` that closes multiple levels of `FOR` is aligned under the first `FOR`.
6. Multiline `IF` statements have their `ELSE`, `ELSEIF` and `ENDIF` aligned under the relevant `IF`. Intervening statements are indented one level.
7. Nesting increases the indent one level.
8. For numbered programs, the line number is left-aligned; the rest of the source uses the longest line number length + 1 as the left margin.
9. Other than setting the indent, the source line is not altered.
10. No attempt is made to check or report program errors.

## Why these rules belong in the course

Most of the hand-typed examples in our lessons follow these conventions implicitly. Calling them out (esp. "labels and SUB to the left margin", "matching LOOP/NEXT/ENDIF aligned with the opener") gives readers a shared vocabulary when they look at community programs from the Back Shed forum or the michaeladcock TiddlyWiki — those are formatted this way too.

---

## Useful internal tables (from the implementation)

The formatter parses lines using two lookups; both are useful as **language reference**.

**Reserved words that may legally be followed by a colon** (so they're never confused with a label):

```
PRINT, RETURN, CLS, RESTORE, CLEAR, EXIT, FILES, MEMORY, NEW,
KEYDOWN, TROFF, TRON, DO, LOOP, NEXT
```

**Operators** (used to disambiguate "variable assignment" from "label"):

```
=  +  -  *  /  <  >  ^
```

A token containing an operator can never be a label — handy mental model when parsing dense lines.

## Source code

The full `Format.bas` (~600 lines, MMBasic 4.x era) is on the wiki. Not bundled here directly; if needed, fetch from the wiki link at top.
