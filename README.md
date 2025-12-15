# Advent of Code 2025 🎄

This repository contains my Python solutions for Advent of Code 2025.  
Each day's solution lives in its own folder:

```
aoc/
  day01/
    solution.py
    input.txt
  day02/
    solution.py
    input.txt
  ...
```

The goal is to keep each day self-contained while sharing helpers via `aoc/utils.py`.

---

## 🚀 Running a Day

Use the included command:

```bash
uv run run.py <day>
```

Examples:

```bash
uv run run.py 1
uv run run.py 01
uv run run.py 10
```

This automatically:

- loads `aoc/dayXX/solution.py`
- reads `aoc/dayXX/input.txt`
- calls `part1()` and `part2()` if they exist
- prints the final answers

---

## 🧰 Project Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Or if using `pyproject.toml`:

```bash
pip install .
```

If using `uv`, create a virtual environment:

```bash
uv venv
```

And then install dependencies:

```bash
uv pip install .
```

---

## 🧪 Running Tests

Run all tests with:

```bash
pytest
```

Or, if using `uv`:

```bash
uv run pytest
```

---

## 📥 (Optional) Auto-Download Inputs

If you want input auto-download before coding:

1. Create a `.env` with:

```
AOC_SESSION=your_session_cookie_here
```

2. Run:

```bash
uv run scripts/download_input.py <day>
```

This saves the input into `aoc/dayXX/input.txt`.

## 📥 (Optional) Auto-Create Day Template

If you want to auto-create a day template, with the solution file & associated test, run:

```bash
uv run scripts/create-day.py <day>
```

---

## 🎄 Structure

```
aoc-2025/
├── run.py
├── pyproject.toml (optional)
├── requirements.txt
├── README.md
│
├── aoc/
│   ├── __init__.py
│   ├── utils.py
│   ├── day01/
│   │   ├── input.txt
│   │   └── solution.py
│   ├── day02/
│   │   ├── input.txt
│   │   └── solution.py
│   └── ...
│
└── tests/
    └── test_day01.py
```

---

## 🎁 Notes

- All days use the shared helpers in `aoc/utils.py` for loading input.
- `part1()` and `part2()` can return any type; the runner will print them.
- Solutions aim to be clean and readable rather than overly golfed.
