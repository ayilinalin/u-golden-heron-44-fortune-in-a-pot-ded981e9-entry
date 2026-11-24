"""Fortune in a Pot — make.fun entry.

Writes one kind, funny fortune for a houseplant (at most 120 characters,
one line) to /output/entry.txt, where the sealed gate scorer reads it.

The fortune is fixed and deterministic: the same line on every run, so the
gate (UTF-8 text, 1-120 characters, not only whitespace) always passes.
"""

import os
import sys

FORTUNE = (
    "The stars say a new leaf unfurls for you by Sunday, "
    "and the whole windowsill will pretend it isn't jealous."
)

MAX_CHARS = 120


def main() -> int:
    out_path = os.environ.get("MAKEFUN_OUTPUT") or "/output/entry.txt"

    text = FORTUNE.strip()
    if not text or len(text) > MAX_CHARS or "\n" in text:
        print("fortune fails the gate", file=sys.stderr)
        return 1

    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(text)

    # Read it back and confirm the file holds exactly what the gate sees.
    with open(out_path, encoding="utf-8") as fh:
        written = fh.read()
    if written != text:
        print("round-trip mismatch", file=sys.stderr)
        return 1

    print(f"wrote {len(text)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
