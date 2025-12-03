import os
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv()

SESSION = os.getenv("AOC_SESSION")
YEAR = 2025


def download(day):
    url = f"https://adventofcode.com/{YEAR}/day/{day}/input"
    cookies = {"session": SESSION}
    resp = requests.get(url, cookies=cookies)

    day_folder = Path(f"aoc/day{day:02d}")
    day_folder.mkdir(parents=True, exist_ok=True)

    (day_folder / "input.txt").write_text(resp.text.rstrip("\n"))


if __name__ == "__main__":
    import sys

    download(int(sys.argv[1]))
