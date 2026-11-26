"""The Printer Finally Answers.

Writes the office printer's one-line comeback to /output/entry.txt.
Pure standard library, deterministic: the same line every run.
"""

import os

LINE = (
    "You pressed print 47 times for one document. I printed it once. "
    "The other 46 copies are in the tray, and every thump has been "
    "logged as a separate incident."
)


def main() -> None:
    # The gate requires 1-240 characters of non-blank UTF-8 text.
    assert 1 <= len(LINE) <= 240 and LINE.strip(), "entry line out of bounds"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
