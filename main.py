"""Write the excuse line to /output/entry.txt.

Pure stdlib, deterministic: the same bytes on every run.
"""

import os

PART_A = "Morning boss, my upstairs neighbour's pipe burst and my kitchen "
PART_B = "ceiling is coming down, waiting on the emergency plumber."

LINE = PART_A + PART_B
assert LINE == (
    "Morning boss, my upstairs neighbour's pipe burst and my kitchen "
    "ceiling is coming down, waiting on the emergency plumber."
)
assert 1 <= len(LINE) <= 140
assert len(LINE.split()) <= 20


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
