# Graphics — quick reference

> Source: <https://yamavu.github.io/PicoMite_User_Manual/graphics_functions.html>
> Mirror of the PicoMite User Manual graphics chapter. Fetched 2026-05-17.
> Full-fidelity version is in the [PDF](PicoMite_User_Manual.pdf) (chapter "Graphics Functions"). This is a condensed quick reference.

---

## Colour

24-bit RGB. Build with:

```basic
RGB(red, green, blue)         ' 0..255 each
RGB(red)                       ' or named: black, blue, green, cyan, red,
                               ' magenta, yellow, brown, white, orange, pink,
                               ' gold, salmon, beige, lightgrey, grey
                               ' (US: gray / lightgray)
```

Set per-program defaults once:

```basic
COLOUR foreground, background       ' COLOR also accepted
```

Drawing commands without explicit colour use these defaults.

## Built-in fonts

| Font | Size (W×H) | Notes |
|---|---|---|
| 1 | 8×12 | default; full ASCII + 7F–FF |
| 2 | 12×20 | medium |
| 3 | 16×16 (VGA) / 16×24 (LCD) | large |
| 4 | 10×16 | extended graphics chars |
| 5 | 24×32 | extra large |
| 6 | 32×50 | digits + symbols only (incl. `°`, `:`, `=`) |
| 7 | 6×8 | small |
| 8 | 4×6 | tiny |

In all fonts the back-quote `` ` `` (60 hex) is replaced with the degree symbol `°`.

Embed extra fonts via `DefineFont … END DefineFont` blocks anywhere in your program.

## Screen geometry

- Coordinates in pixels. Top-left = `(0, 0)`. X grows right, Y grows down.
- Read-only variables:
  - `MM.HRES` — width in pixels (PicoCalc: 320)
  - `MM.VRES` — height in pixels (PicoCalc: 320)
  - `MM.INFO(FONTHEIGHT)` — current font height
  - `MM.INFO(FONTWIDTH)`  — current font width

## Drawing commands

Optional parameters can be skipped with `,,`. `C` = drawing colour (default = foreground), `FILL` = fill colour (default `-1` = no fill).

```basic
CLS [C]
PIXEL X, Y [, C]
LINE X1, Y1, X2, Y2 [, LW] [, C]
BOX X, Y, W, H [, LW] [, C] [, FILL]
RBOX X, Y, W, H [, R] [, C] [, FILL]            ' rounded box, R = corner radius
CIRCLE X, Y, R [, LW] [, A] [, C] [, FILL]      ' A = aspect (oval)
ARC x, y, r1 [, r2], a1, a2 [, c]                ' arc between two radials, 0° = 12 o'clock
POLYGON n, xarray%(), yarray%() [, bordercolour] [, fillcolour]
TEXT X, Y, STRING [, ALIGNMENT] [, FONT] [, SCALE] [, C] [, BC]
GUI BITMAP X, Y, BITS, WIDTH, HEIGHT [, SCALE] [, C] [, BC]
```

`LW` (line width) is only honoured for horizontal/vertical lines and box outlines. For diagonal lines with width use the extended `LINE AAA` form (see PDF).

## Text alignment / rotation

`ALIGNMENT` is 1–3 characters in a string:

- 1st char (horizontal): `L` left, `C` centre, `R` right (around X). Default: `L`.
- 2nd char (vertical): `T` top, `M` middle, `B` bottom (around Y). Default: `T`.
- 3rd char (rotation): `N` normal, `V` vertical (each char under the previous), `I` inverted, `U` rotated CCW 90°, `D` rotated CW 90°.

```basic
TEXT 160, 0,   "Title", "CT", 5             ' centred horizontally, top-aligned, font 5
TEXT 0, 250,   "LCD Display", "LMV", 5      ' vertical text down the left margin
```

## Bitmap I/O

```basic
SAVE IMAGE "out.bmp", x, y, w, h         ' save region as 24-bit BMP
LOAD IMAGE "out.bmp"                      ' draw a BMP at (0,0)
```

Useful for screenshots and pre-rendered art (the `picocalc.bmp` and `out.bmp` already on the SD card are examples of this).

## Framebuffer (off-screen drawing) — for animation

```basic
FRAMEBUFFER CREATE F                  ' create off-screen buffer F
FRAMEBUFFER WRITE F                   ' subsequent draw commands target F
FRAMEBUFFER COPY F, N [, transparent] ' copy F to N (N = display)
FRAMEBUFFER WRITE N                   ' switch back to direct screen drawing
FRAMEBUFFER CLOSE
```

The double-buffer pattern: draw a full frame into `F`, copy `F` to `N` once per frame — eliminates flicker. Critical for lesson 04 (Графика) and 08 (Capstone).

## Sprites

The PicoMite has a hardware-style sprite system layered on top of FRAMEBUFFER. See the manual chapter "Sprite Format" and `SPRITE` commands. Useful for games (lesson 08).

## Convention notes

- British spelling **`COLOUR`** is canonical; `COLOR` is accepted as an alias. The same goes for `GREY` / `GRAY`. Prefer `COLOUR/GREY` to match the manual.
- All measurements are pixels. There is no point/em concept.
- The PicoCalc display is **320×320 portrait** (`OPTION LCDPANEL ILI9488P, PORTRAIT, …`). All examples should fit inside this.
