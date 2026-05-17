# LennartHennigs / PicoCalc-Notes — README

> Source: <https://github.com/LennartHennigs/PicoCalc-Notes>
> Lennart Hennigs' personal notes & programs for the PicoCalc. Fetched 2026-05-17.

The same content also lives in <https://github.com/LennartHennigs/PicoCalc>. Lennart maintains the (separately tracked) **MMBasic Style Guide** in `src/CLAUDE.md` of the same repo (mirrored locally as `references/community/mmbasic_style_guide.md`).

---

## Hardware

- comes with a [Raspberry Pi Pico](https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html#pico-1-family)
- Pin-compatible devices can also be used, but need a new firmware, e.g.
  - Pico 2W
  - [Luckfox Lyra](https://wiki.luckfox.com/Luckfox-Lyra/Introduction/)

### Pico Pinout

- See [pico.pinout.xyz](https://pico.pinout.xyz/) for the Pico pinout.
- Used pins:
  - **I2C**: GP6, GP7 (hardwired to built-in keyboard)
  - **SPI** (LCD): GP10, GP11, GP12
  - **SD Card**: GP17, GP18, GP19, GP16
  - **Audio** (PWM): GP26, GP27
- Available via pin headers:
  - GP2, GP3, GP4, GP5, GP21, GP28

### LCD

- ILI9488P, controlled via SPI
- Screen Resolution: 320×320 px

### Hardware Hacks

- [RGB LED Stick](https://steinlaus.de/rgb-led-stick-fuer-den-picocalc/)
- [RTC](https://forum.clockworkpi.com/t/rtc-inside-the-case/16484) (Real-time Clock)
- [LoRa](https://forum.clockworkpi.com/t/picocalc-with-lora/16773) via an ESP32 LoRa board
- [Pi Zero 2 replacement](https://forum.clockworkpi.com/t/raspberry-pi-zero-2-on-picocalc/17946)

## Firmware

### MMBasic

- [MMBasic branch for PicoCalc](https://github.com/madcock/PicoMiteAllVersions)
- [MMBasic Manual (PDF)](https://geoffg.net/Downloads/picomite/PicoMite_User_Manual.pdf)

### Updating the Firmware

- Press BOOTSEL on the Pi Pico
- Plug in the device using the **Mini USB** connector
- The PicoCalc appears as a drive
- Copy the `.uf2` file
- Eject and unplug
- Reboot

## Connecting via Serial

- Use the **USB-C** connector
- Use a terminal program (e.g., [tio](https://github.com/tio/tio) or [minicom](https://formulae.brew.sh/formula/minicom) on a Mac):
  - `tio /dev/tty.usbserial-110`
  - `minicom -D /dev/tty.usbserial-110 -b 115200 -c`
- Settings:
  - 115200 baud
  - 8N1
  - Emulation VT102
  - Backspace key: BS
  - Enable VT102 color mode

### File Transfer via Serial

- On the PicoCalc: `XMODEM RECEIVE`
- In the terminal program: send via XModem.

## MMBasic Tips

### Pre-defined Shortcuts (at REPL)

| Key | Command |
|---|---|
| F2 | RUN |
| F3 | LIST |
| F4 | EDIT |
| F10 | AUTOSAVE |
| Ctrl+C | Exit program |

### Defining additional shortcuts (F1, F5–F9)

```basic
OPTION F5 "DRIVE " + CHR$(34) + "B:" + CHR$(13)
```

### MMBasic Options

```basic
' show current options
OPTION LIST

' will automatically run the program in program memory
OPTION AUTORUN ON

' disable Pico LED blinking
OPTION HEARTBEAT OFF
```

### Editor Options

```basic
' keyword display in edit [lower|upper|title]
OPTION CASE LOWER

' colors in edit
OPTION COLORCODE ON

' line wrap in edit (needs MMBasic >= 6.x)
OPTION CONTINUATION LINES ON
```

## Helpful Commands

### Access SD Card

```basic
DRIVE "B:"
FILES
```

### Invoking the Editor

```basic
EDIT
```

### Take a Screenshot & load it

```basic
SAVE IMAGE "out.bmp", 0, 0, 319, 319
...
LOAD IMAGE "out.bmp"
```
