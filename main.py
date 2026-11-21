#!/usr/bin/env python3
"""Entry for make.fun's "The joke the reviewer laughs at" bounty.

Writes a single one-line joke about working beside AI coding agents
to /output/entry.txt. Deterministic, no network, stdlib only.
"""

import os

JOKE = (
    "My AI pair programmer writes a thousand lines before my coffee cools, "
    "so my job is now reading a stranger's homework and deciding whether "
    "to sign it."
)


def main() -> None:
    # The competition requires 1-280 characters on one line: fail loudly
    # instead of writing an entry the gate would reject.
    assert 1 <= len(JOKE) <= 280, f"joke is {len(JOKE)} chars, must be 1-280"
    assert "\n" not in JOKE, "joke must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
