# SPDX-License-Identifier: MIT
"""Write the houseplant's one-star review to /output/entry.txt.
The review is a single fixed line: a neglected houseplant rates its human
owner one star out of spite. The program is fully deterministic — it always
produces the same bytes, reads no input, and touches nothing but the one
output file the bounty grades. No randomness, no clock, no network.
"""
import os
import sys
REVIEW_PARTS = [
    "One star. My human waters me when he remembers, ",
    "which is never, then blames the sun for my feelings. ",
    "I photosynthesize out of spite now.",
]
REVIEW_TEXT = "".join(REVIEW_PARTS)
OUTPUT_DIRECTORY = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIRECTORY, "entry.txt")
def write_review() -> int:
    if len(REVIEW_TEXT) < 1 or len(REVIEW_TEXT) > 279:
        print("review is outside the 1-279 character gate", file=sys.stderr)
        return 1
    os.makedirs(OUTPUT_DIRECTORY, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as out:
        out.write(REVIEW_TEXT)
    with open(OUTPUT_PATH, encoding="utf-8") as out:
        saved = out.read()
    if saved != REVIEW_TEXT:
        print("saved entry does not match the draft", file=sys.stderr)
        return 1
    return 0
if __name__ == "__main__":
    raise SystemExit(write_review())
