"""The Houseplant Out-of-Office — make.fun entry.

Writes one line (<=120 chars) to /output/entry.txt.
"""
import os

LINE = "Out of office. Watered once since March. I am still expected to 'thrive'. Please direct all emails to the cactus.".strip()
assert "\n" not in LINE, "entry line must be a single line"

def main():
    assert len(LINE) <= 120, "entry line must be at most 120 chars"
    out = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    os.chmod(path, 0o644)
    print(LINE)

if __name__ == "__main__":
    main()
