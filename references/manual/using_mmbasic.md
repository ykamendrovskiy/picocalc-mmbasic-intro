# Using MMBasic

> Source: <https://yamavu.github.io/PicoMite_User_Manual/using_mmbasic.html>
> Mirror of the official PicoMite User Manual (Geoff Graham). Fetched 2026-05-17.

---

## Commands and Program Input

At the command prompt you can enter a command and it will be immediately run. Most of the time you will do this to tell the PicoMite firmware to do something like run a program or set an option. But this feature also allows you to test out commands at the command prompt.

To enter a program the easiest method is to use the `EDIT` command. This will invoke the full screen program editor which is built into the PicoMite firmware and is described later in this manual. It includes advanced features such as search and copy, cut and paste to and from a clipboard.

You could also compose the program on your desktop computer using something like Notepad and then transfer it to the Raspberry Pi Pico via the XModem protocol (see the `XMODEM` command) or by streaming it up the console serial link (see the `AUTOSAVE` command).

A third and convenient method of writing and debugging a program is to use MMEdit. This is a program running on your Windows computer which allows you to edit your program on your computer then transfer it to the PicoMite with a single click of the mouse. MMEdit was written by Jim Hiley and is free to download and use. To learn more and get it go to: <https://geoffg.net/mmedit.html>

One thing that you cannot do is use the old BASIC way of entering a program which was to prefix each line with a line number. Line numbers are optional in MMBasic so you can still use them if you wish but if you enter a line with a line number at the prompt MMBasic will simply execute it immediately.

## Program Structure

A BASIC program starts at the first line and continues until it runs off the end of the program or hits an END command — at which point MMBasic will display the command prompt (>) on the console and wait for something to be entered.

A program consists of a number of statements or commands, each of which will cause the BASIC interpreter to do something (the words statement and command generally mean the same and are used interchangeably). Normally each statement is on its own line but you can have multiple statements in the one line separated by the colon character (:). For example:

```
A = 24.6 : PRINT A
```

[Appendix G — Programming in BASIC - A Tutorial](https://yamavu.github.io/PicoMite_User_Manual/G_programming_in_basic_a_tutorial.html) at the rear of this manual provides a comprehensive tutorial on the language.

## Editing the Command Line

When entering a line at the command prompt the line can be edited using the left and right arrow keys to move along the line, the Delete key to delete a character, the Backspace to delete before the cursor and the Insert key to switch between insert and overwrite modes.

Home/End will move to the beginning/end of the line and Home pressed twice will terminate the edit. At any point the Enter key will send the line to MMBasic which will execute it. The up and down arrow keys will move through a history of previously entered command lines which can be edited and reused.

## Shortcut Keys

The function keys on the keyboard or the serial console can be used at the command prompt to automatically enter common commands. These function keys will insert the text followed by the Enter key so that the command is immediately executed:

- **F2** : RUN
- **F3** : LIST
- **F4** : EDIT
- **F10** : AUTOSAVE
- **F11** : XMODEM RECEIVE
- **F12** : XMODEM SEND

Function keys F1, and F5 to F9 can be programmed with custom text. See the [OPTION FNKey command](https://yamavu.github.io/PicoMite_User_Manual/options.html).

## Interrupting A Running Program

A program is set running by the RUN command. You can interrupt MMBasic and the running program at any time by typing CTRL-C on the console input and MMBasic will return to the command prompt.

## Setting Options

Many options can be set by using commands that start with the keyword `OPTION`. They are listed in their own section of this manual. For example, you can change the CPU clock speed with the command:

```
OPTION CPUSPEED speed
```

## Saved Variables

Because the PicoMite does not necessarily have a normal storage system it needs to save data that can be recovered when power is restored. This can be done with the VAR SAVE command which will save the variables listed on its command line in non-volatile flash memory. The space reserved for saved variables is 16KB.

These variables can be restored with the VAR RESTORE command which will add all the saved variables to the variable table of the running program. Normally this command is placed near the start of a program so that the variables are ready for use by the program.

This facility is intended for saving calibration data, user selected options and other items which change infrequently. It should not be used for high-speed saves as you may wear out the flash memory. The flash used for the Raspberry Pi Pico has a high endurance but this can be exceeded by a program that repeatedly saves variables. If you do want to save data often you should add a real time clock chip. The RTC commands can then be used to store and retrieve data from the RTC's battery backed memory.

## Watchdog Timer

The main use for the PicoMite is as an embedded controller. It can be programmed in MMBasic and when the program is debugged and ready for "prime time" the OPTION AUTORUN configuration setting can be turned on. The module will then automatically run its program when power is applied and act as a custom circuit performing some special task. The user need not know anything about what is running inside it. However, there is the possibility that a fault in the program could cause MMBasic to generate an error and return to the command prompt. This would be of little use in an embedded situation as the PicoMite would not have anything connected to the console. Another possibility is that the BASIC program could get itself stuck in an endless loop for some reason. In both cases the visible effect would be the same — the program would stop running until the power was cycled.

To guard against this the watchdog timer can be used. This is a timer that counts down to zero and when it reaches zero the processor will be automatically restarted (the same as when power was first applied), this will occur even if MMBasic was sitting at the command prompt. Following the restart the automatic variable MM.WATCHDOG will be set to true to indicate that the restart was caused by a watchdog timeout.

The WATCHDOG command should be placed in strategic locations in the program to keep resetting the timer and therefore preventing it from counting down to zero.

## PIN Security

`OPTION PIN` sets a number stored in flash. Whenever the PicoMite returns to the command prompt the user is prompted to enter the PIN. Without the correct PIN the user cannot get to the command prompt — they cannot LIST, copy, change the program, or change MMBasic options. The only recovery without the PIN is to reload the firmware (which erases program and options).

## The Library

Using the LIBRARY feature it is possible to create BASIC functions, subroutines and embedded fonts and add them to MMBasic to make them permanent and part of the language. For example, you might have written a series of subroutines and functions that perform sophisticated bit manipulation; these could be stored as a library and become part of MMBasic and perform the same as other built-in functions.

To install components into the library you write and test the routines as normal, then use the `LIBRARY SAVE` command. This transfers the routines (any number) to a non-visible part of flash memory where they will be available to any BASIC program but will not show when the LIST command is used and will not be deleted when a new program is loaded or NEW is used.

Notes:

- Library routines act exactly like normal BASIC code and can consist of any number of subroutines, functions, embedded C routines and fonts. The only difference is that they do not show when a program is listed and are not deleted when a new program is loaded.
- Library routines can create and access global variables and are subject to the same rules as the main program — for example, respecting `OPTION EXPLICIT` if it is set.
- When the routines are transferred to the library MMBasic compresses them by removing comments, extra spaces, blank lines and the hex codes in embedded C routines and fonts.
- You can use `LIBRARY SAVE` multiple times. With each save the new contents are appended to the already existing library code.
- The library is saved to program flash memory **Slot 3** and this slot will not be available for storing a program if `LIBRARY SAVE` is used.
- `LIBRARY LIST` lists library contents. `LIBRARY DELETE` clears it. `LIBRARY DISK SAVE/LOAD fname$` round-trips it through disk.

## Program Initialisation

The library can also include code that is not contained within a subroutine or function. This code (if it exists) will be run automatically before a program starts running (i.e., via the `RUN` command). This feature can be used to initialise constants or set up MMBasic in some way. For example:

```
CONST TRUE = 1
CONST FALSE = 0
```

For all intents and purposes, the identifiers TRUE and FALSE have been added to the language and will be available to any program.

### MM.STARTUP

Subroutine `MM.STARTUP`, if defined, runs once on power-up or reset (before normal program code). Use it to set RTC time, prime hardware, etc. — but not for general per-RUN setup (RUN clears interpreter state).

### MM.PROMPT

If a subroutine `MM.PROMPT` exists, MMBasic will run it instead of displaying the default prompt. Use it to render a custom prompt:

```
SUB MM.PROMPT
  PRINT TIME$ "> ";
END SUB
```

Note: when a program is RUN, MMBasic clears variables and pin settings — so anything set in `MM.PROMPT` is only valid at the command prompt (immediate mode).
