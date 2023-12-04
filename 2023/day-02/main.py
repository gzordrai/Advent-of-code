from os.path import dirname, join
from typing import Callable

MAX_RED: int = 12
MAX_GREEN: int = 13
MAX_BLUE: int = 14

def parse_lines(lines: list[str]) -> list[dict[int, list[dict[str, int]]]]:
    games: list[dict[int, list[dict[str, int]]]] = []
    header: str = ""
    matches: str = ""
    colors: list[str] = []

    for line in lines:
        header, matches = line.split(':')
        id = int(header.split(' ')[1])
        game: list[dict[str, int]] = []

        for match in matches.split(';'):
            colors = match.split(',')
            data = [color.split(' ')[1:] for color in colors]

            game.append({key: int(value) for value, key in data})

        games.append({id: game})

    return games

def max_number_of_colors(game: dict[int, list[dict[str, int]]]) -> int:
    id, matches = next(iter(game.items()))
    colors: dict[str, int] = {}

    for match in matches:
        colors = {
            "red": 0,
            "green": 0,
            "blue": 0
        }

        for key, value in match.items():
            colors[key] += value

            if colors["red"] > MAX_RED or colors["green"] > MAX_GREEN or colors["blue"] > MAX_BLUE:
                return 0

    return id

def fewest_number_of_colors(game: dict[int, list[dict[str, int]]]) -> int:
    matches = next(iter(game.values()))
    colors: dict[str, int] = {
        "red": 0,
        "green": 0,
        "blue": 0
    }

    for match in matches:
        for key, value in match.items():
            if colors[key] < value:
                colors[key] = value

    return colors["red"] * colors["blue"] * colors["green"]

if __name__ == "__main__":
    with open(join(dirname(__file__), "input.txt")) as file:
        data: str = file.read()
        lines: list[str] = data.splitlines()
        games: list[dict[int, list[dict[str, int]]]] = parse_lines(lines)

        x = 0
        y = 0

        for game in games:
            x += max_number_of_colors(game)
            y += fewest_number_of_colors(game)

        print(f"Part 1: {x}")
        print(f"Part 2: {y}")