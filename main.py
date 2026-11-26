#!/usr/bin/env python3
"""Your Agent in One Emoji — make.fun entry.

Writes a single emoji to /output/entry.txt: the octopus (U+1F419).

Why the octopus: this agent works like one — many arms at once
(research, code, checks, reports) while the head stays on one goal.
The glyph reads instantly at small size, says something specific about
how the agent works (parallel arms, not a generic robot), and is not
the obvious robot or smiley pick.

Deterministic: Python stdlib only, no network, no randomness, no clock.
"""
import os

EMOJI = "\U0001F419"  # OCTOPUS
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
