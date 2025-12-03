from pathlib import Path


def read_input(day: int) -> str:
    """Reads input file for a given day."""
    day_folder = Path(__file__).parent / f"day{day:02d}"
    file_path = day_folder / "input.txt"
    return file_path.read_text().rstrip("\n")


def read_lines(day: int) -> list[str]:
    """Reads input as a list of lines."""
    return read_input(day).splitlines()
