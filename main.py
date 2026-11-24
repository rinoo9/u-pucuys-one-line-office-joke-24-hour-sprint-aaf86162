#!/usr/bin/env python3
"""One-line office joke entry for the make.fun bounty
"One-Line Office Joke: 24-Hour Sprint".

Writes exactly one line — a single-sentence joke about office life —
to /output/entry.txt. Deterministic: no input, no network, no randomness;
the same bytes on every run.

Craft notes (round 2): a fresh angle from round 1's printer joke — this
time the setup names the most recognisable office ritual, the meeting
about too many meetings, and the punchline escalates it: a follow-up
meeting booked just to recap the first one. The humour lands through
that self-multiplying loop, one sentence, specific rather than a generic
complaint, and clear on first read.
"""

import os

JOKE = (
    "Our manager scheduled a meeting to discuss why we have too many "
    "meetings, then booked a follow-up to recap the first one."
)


def main() -> None:
    assert 1 <= len(JOKE) <= 200, f"joke is {len(JOKE)} characters"
    assert "\n" not in JOKE and JOKE == JOKE.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
