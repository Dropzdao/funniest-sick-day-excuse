#!/usr/bin/env python3
"""Funniest Sick-Day Excuse — make.fun bounty entry.

Writes one line (the entry) to /output/entry.txt, with no trailing newline.
Deterministic: no network, no randomness, no input.
"""

import os

ENTRY = "Sorry, can't come in \u2014 my smart fridge locked me out of the kitchen and I've been negotiating with it since 6am."

# The line is 112 characters, a single line, UTF-8 — inside the gate's 1-200 range.
# Craft notes: the setup (a smart fridge locking its owner out) is half
# believable, the idea is fresh (no fever, no dog, no dead grandmother),
# and the laugh lands on the last words — "negotiating with it since 6am" —
# which sounds like a real person texting their boss, not a contest joke.


def main() -> None:
    # Guard the gate at runtime: 1-200 chars, single line, not only whitespace.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY and ENTRY.strip(), "entry must be one non-blank line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
