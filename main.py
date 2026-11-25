"""Entry for the make.fun bounty 'Have You Tried Turning It Off?'.

Writes one funny tech-support line to /output/entry.txt.
Set OUTPUT_FILE to override the destination for local testing.
"""

import os

LINE = (
    "Great news — I've fixed this exact issue before, on this very call, "
    "with you, so we already know the steps and we get to enjoy them all "
    "again together!"
)


def main() -> None:
    path = os.environ.get("OUTPUT_FILE", "/output/entry.txt")
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
