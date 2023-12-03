from typing import Callable

DIGITS: list[str] = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def parse_digits(line: str) -> list[int]:
    ret = []
    buffer = ""
    k = 0

    for c in line:
        if c.isdigit():
            ret.append(int(c))
            buffer = ""
            continue

        buffer += c

        for i in range(len(DIGITS)):
            if DIGITS[i].startswith(buffer):
                if buffer in DIGITS:
                    ret.append(i + 1)
                    buffer = buffer[-1]
                    break
            else:
                k += 1

        if k == len(DIGITS):
            buffer = buffer[1:]

        k = 0

    return ret

def parse_int(line: str) -> list[int]:
    digits: list[str] = "".join(filter(str.isdigit, line))

    return list(map(int, digits))

def parse_lines(parser: Callable[[str], list[int]], lines: list[str]) -> list[int]:
    ret = []
    result: list[int] = []

    for line in lines:
        result = parser(line)
        ret.append(result[0] * 10 + result[-1])

    return ret

if __name__ == "__main__":
    with open("./input.txt") as file:
        data: str = file.read()
        lines: list[str] = data.splitlines()

        print(f"Part 1: {sum(parse_lines(parse_int, lines))}")
        print(f"Part 2: {sum(parse_lines(parse_digits, lines))}")