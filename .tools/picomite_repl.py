# /// script
# dependencies = ["pyserial"]
# ///
"""
Send commands to a PicoMite REPL over USB serial and capture responses.

Usage:
    uv run picomite_repl.py [--port /dev/cu.usbmodemXXX] [--timeout SEC] <<< 'PRINT MM.HRES'
    uv run picomite_repl.py --port /dev/cu.usbmodem11301 -c 'PRINT MM.HRES' -c 'PRINT MM.VRES'

Reads commands from -c flags or stdin (one per line), prints what came back.
"""
import argparse
import sys
import time

import serial


PROMPT = b">"


def open_port(port: str, baud: int = 115200) -> serial.Serial:
    s = serial.Serial(port, baudrate=baud, timeout=0.1)
    time.sleep(0.2)
    s.reset_input_buffer()
    return s


def send_cmd(s: serial.Serial, cmd: str, settle: float = 0.05, max_wait: float = 5.0) -> str:
    s.write(cmd.encode("utf-8") + b"\r")
    s.flush()
    time.sleep(settle)
    deadline = time.time() + max_wait
    buf = bytearray()
    while time.time() < deadline:
        chunk = s.read(4096)
        if chunk:
            buf.extend(chunk)
            if buf.rstrip().endswith(PROMPT):
                break
        else:
            if buf and buf.rstrip().endswith(PROMPT):
                break
    return buf.decode("utf-8", errors="replace")


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--port", default="/dev/cu.usbserial-10")
    p.add_argument("--baud", type=int, default=115200)
    p.add_argument("-c", "--cmd", action="append", default=[],
                   help="Command to send (repeatable). If absent, reads stdin.")
    p.add_argument("--max-wait", type=float, default=5.0)
    args = p.parse_args()

    cmds = args.cmd if args.cmd else [ln.rstrip("\n") for ln in sys.stdin if ln.strip()]
    if not cmds:
        print("(no commands)", file=sys.stderr)
        return 1

    try:
        s = open_port(args.port, args.baud)
    except serial.SerialException as e:
        print(f"open failed: {e}", file=sys.stderr)
        return 2

    try:
        send_cmd(s, "", max_wait=1.0)
        for c in cmds:
            print(f"\n>>> {c}")
            print(send_cmd(s, c, max_wait=args.max_wait), end="")
    finally:
        s.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
