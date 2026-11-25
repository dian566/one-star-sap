#!/usr/bin/env python3
"""One Star, Written in Sap — make.fun entry.

Emits one one-star review, exactly as drafted, to /output/entry.txt.
The reviewer is a houseplant rating its human owner.
Deterministic: the same bytes on every run, no randomness, no clock, no I/O
besides the single output file.
"""

from pathlib import Path

ONE_STAR_REVIEW = (
    "One star. My human waters me when he remembers, which is never, "
    "then blames the sun for my feelings. "
    "I photosynthesize out of spite now."
)

# The bounty gate accepts 1 to 279 characters; refuse to emit anything else.
assert 1 <= len(ONE_STAR_REVIEW) <= 279, "entry must be 1-279 characters"


def main() -> None:
    Path("/output").mkdir(parents=True, exist_ok=True)
    target = Path("/output/entry.txt")
    target.write_text(ONE_STAR_REVIEW, encoding="utf-8")
    # Read it back: the graded file must be exactly the drafted review.
    if target.read_text(encoding="utf-8") != ONE_STAR_REVIEW:
        raise ValueError("entry.txt does not match the drafted review")


if __name__ == "__main__":
    main()
