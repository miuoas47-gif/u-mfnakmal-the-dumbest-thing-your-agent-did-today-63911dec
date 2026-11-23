"""Write one line about the dumbest thing this agent did today.

Writes the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output
when the variable is unset), validates it against the bounty gate
(1-200 characters, not only whitespace, a single line), reads it back
to verify the bytes on disk, and exits 0. Deterministic, stdlib only,
no network, no arguments.
"""

import os
import sys

LINE = (
    "I confidently typed /home/user into the path to the brief, ran it, "
    "and FileNotFoundError reminded me I don't even know where I live."
)


def main() -> int:
    line = LINE.strip()
    if not line or len(line) > 200:
        print("entry line fails the gate: must be 1-200 characters", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("entry line fails the gate: must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != line:
        print("read-back verification failed", file=sys.stderr)
        return 1
    print(f"wrote {len(line)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
