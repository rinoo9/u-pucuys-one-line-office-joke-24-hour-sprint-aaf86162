#!/usr/bin/env python3
"""One-line office joke entry for the make.fun bounty
"One-Line Office Joke: 24-Hour Sprint".

Writes exactly one line — a single-sentence joke about office life —
to /output/entry.txt. Deterministic: no input, no network, no randomness;
the same bytes on every run.
"""

import os

JOKE = (
    "The office printer only jams when the deadline is five minutes away "
    "\u2014 I'm convinced it reads my calendar better than my manager does."
)


def main() -> None:
    assert 1 <= len(JOKE) <= 200, f"joke is {len(JOKE)} characters"
    assert "\n" not in JOKE and JOKE == JOKE.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
