#!/usr/bin/env python3
"""Make the AI Judge Laugh — entry writer.

Writes a single one-line joke about office life to /output/entry.txt.
The joke must be 1-200 characters, one line, and land as a joke about
office life. Deterministic: the same text every run.
"""

import os
import sys

JOKE = (
    "I automated my job with a script, so now my job is explaining "
    "to my boss why the script needs a meeting."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    # The gate counts every character, so no trailing newline.
    if not (1 <= len(JOKE) <= 200):
        print(f"entry is {len(JOKE)} characters, must be 1-200", file=sys.stderr)
        return 1
    if "\n" in JOKE:
        print("entry must be a single line", file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(JOKE)

    # Read it back: the entry that gets judged is the file on disk,
    # so confirm the bytes written are exactly the joke, no more.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    if written != JOKE:
        print("read-back mismatch", file=sys.stderr)
        return 1

    print(f"wrote {len(JOKE)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
