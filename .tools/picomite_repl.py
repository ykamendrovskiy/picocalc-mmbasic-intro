# /// script
# dependencies = ["pyserial"]
# ///
"""
Send commands to a PicoMite REPL over USB serial and capture responses.

Usage:
    uv run picomite_repl.py -c 'PRINT MM.HRES'           # auto-detects port
    uv run picomite_repl.py --port /dev/cu.usbserial-X -c 'PRINT MM.VRES'
    uv run picomite_repl.py <<< 'PRINT MM.HRES'          # commands from stdin

By default, scans /dev/cu.usbserial-* and uses the only matching port.
If multiple match, lists them and exits — pass --port explicitly.
Override with env var PICOMITE_PORT or --port.
"""
import argparse
import glob
import os
import sys
import time

import serial


PROMPT = b">"
PORT_GLOB = "/dev/cu.usbserial-*"


def detect_port() -> str | None:
    candidates = sorted(glob.glob(PORT_GLOB))
    if len(candidates) == 1:
        return candidates[0]
    if len(candidates) > 1:
        print(f"multiple candidates: {candidates}", file=sys.stderr)
        return None
    return None


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
    p.add_argument("--port", default=None,
                   help=f"Serial device. Default: $PICOMITE_PORT or auto-detect ({PORT_GLOB}).")
    p.add_argument("--baud", type=int, default=115200)
    p.add_argument("-c", "--cmd", action="append", default=[],
                   help="Command to send (repeatable). If absent, reads stdin.")
    p.add_argument("--max-wait", type=float, default=5.0)
    args = p.parse_args()

    port = args.port or os.environ.get("PICOMITE_PORT") or detect_port()
    if not port:
        print(f"no port: nothing matched {PORT_GLOB} (and no --port / $PICOMITE_PORT).",
              file=sys.stderr)
        return 2

    cmds = args.cmd if args.cmd else [ln.rstrip("\n") for ln in sys.stdin if ln.strip()]
    if not cmds:
        print("(no commands)", file=sys.stderr)
        return 1

    try:
        s = open_port(port, args.baud)
    except serial.SerialException as e:
        print(f"open failed ({port}): {e}", file=sys.stderr)
        return 2

    print(f"(port: {port})", file=sys.stderr)

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
