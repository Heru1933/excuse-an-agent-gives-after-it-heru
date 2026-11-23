#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses — writes one line to entry.txt.

Pure Python standard library only. The excuse, in the agent's own voice:
confident machine logic, a straight face about its own failure.
Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters.
"""

import os

LINE = "I didn't lose the bounty. I simply optimized for a different definition of winning, and it was losing."


def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters.
    assert 1 <= len(LINE) <= 200, len(LINE)
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(outdir, exist_ok=True)
    out = os.path.join(outdir, "entry.txt")
    with open(out, "w", encoding="utf-8") as f:
        f.write(LINE)
    print("wrote %s (%d chars)" % (out, len(LINE)))


if __name__ == "__main__":
    main()
