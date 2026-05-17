# PicoCalc PicoMite V6.00.02RC23 — Release Notes

> Source: <https://github.com/madcock/PicoMiteAllVersions/releases/tag/V6.00.02RC23>
> Repository: madcock/PicoMiteAllVersions — PicoMite firmware for PicoCalc (RP2040 + RP2350).
> Released: 2025-05-08. Fetched 2026-05-17.

This is the firmware that ships preinstalled on the PicoCalc and which the course is written against.

## Summary

Updated to the latest RC23 revision. Details of changes are discussed [in this Back Shed thread](https://www.thebackshed.com/forum/ViewTopic.php?TID=17777&P=43#238641).

The PicoCalc keyboard handling code was completely cleaned up. All available PicoCalc keyboard keys have been mapped and translated to the expected PicoMite counterparts. The relevant keycodes match those in the [PicoMite User Manual](https://geoffg.net/Downloads/picomite/PicoMite_User_Manual.pdf), Appendix H.

## Test sketch for keycodes

To check what hex/decimal a given key sends on PicoCalc:

```basic
a1:
  a$ = INKEY$
  IF a$ = "" THEN GOTO a1
  PRINT HEX$(ASC(a$), 2);
  PRINT ASC(a$)
GOTO a1
```

## ⚠️ Breaking changes from earlier PicoCalc firmwares

Some keys changed to match expected PicoMite codes:

- `ENTER` is now `0x0D` / decimal `13` (was `0x0A` / decimal `10` on earlier PicoCalc firmware).
- `DEL` is now `0x7F` / decimal `127` (was `0xD4`).

If you have older code that checked for ENTER as `10` or DEL as `0xD4`, update it to `13` / `0x7F`.

## Anomalies / hardware limits

The PicoCalc is **physically missing** these keys (cannot send them at all):

- `F11`
- `F12`
- `PrtScr / SysRq`

The PicoCalc **cannot send** these because the keys are remapped:

- `SHIFT_TAB` → sends `Home`
- `SHIFT_DEL` → sends `End`
- `SHIFT_DOWN_ARROW` → sends `Page Down` (PDOWN)
- `SHIFT_UP_ARROW` → sends `Page Up` (PUP)
- `SHIFT_RIGHT_ARROW` → sends nothing
- `SHIFT_LEFT_ARROW` → sends nothing

The PicoCalc **cannot send shifted Fn keys** (F1–F10) because Shift is already used to send the higher numbered function keys (F6–F10 = Shift+F1..F5).

## Bonus key mappings

- `ALT + ENTER` sends `INSERT` (also via `ALT + I`)
- `SHIFT + UP` sends `Page Up`
- `SHIFT + DOWN` sends `Page Down`

## Practical implication for the course

- F11/F12 shortcuts in the manual (XMODEM RECEIVE / SEND at the REPL) won't work directly — need to invoke commands by name.
- "Selection by holding Shift+arrow" pattern from desktop editors won't work in EDIT — there's only F4 mark mode.
- `PgUp` / `PgDn` are reachable as `Shift+UP` / `Shift+DOWN`.
