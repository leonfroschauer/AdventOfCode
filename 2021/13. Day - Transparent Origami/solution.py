from re import match

with open("input.txt") as file:
    puzzle = file.read().strip()
    plines = puzzle.splitlines()


def part_1():
    coordinates = set(tuple(map(int, line.split(","))) for line in puzzle.split("\n\n")[0].split("\n"))
    d, coord = match(r"fold along (.)=(\d+)$", puzzle.split("\n\n")[1].splitlines()[0]).groups()
    new_grid = set()
    for x, y in coordinates:
        new_grid.add((min(x, 2 * int(coord) - x) if d == "x" else x, min(y, 2 * int(coord) - y) if d == "y" else y))
    return len(new_grid)


print(part_1())


def part_2():
    coordinates = set(tuple(map(int, line.split(","))) for line in puzzle.split("\n\n")[0].split("\n"))
    for line in puzzle.split("\n\n")[1].split("\n"):
        d, coord = match(r"fold along (.)=(\d+)$", line).groups()
        new_grid = set()
        for x, y in coordinates:
            new_grid.add((min(x, 2 * int(coord) - x) if d == "x" else x, min(y, 2 * int(coord) - y) if d == "y" else y))
        coordinates = new_grid

    # The convert function is copied from Defelo (https://github.com/Defelo)
    # https://github.com/Defelo/AdventOfCode/blob/master/2021/13.ipynb
    out = ""
    n = 0
    while True:
        k = 0
        for i in range(5 * n, 5 * n + 4):
            for j in range(6):
                k <<= 1
                k |= (i, j) in coordinates
        if not k:
            break
        out += {
            0b011111100100100100011111: "A",
            0b111111101001101001010110: "B",
            0b011110100001100001010010: "C",
            0b111111101001101001100001: "E",
            0b111111101000101000100000: "F",
            0b011110100001100101010111: "G",
            0b111111001000001000111111: "H",
            0b000010000001100001111111: "J",
            0b111111001000010110100001: "K",
            0b111111000001000001000001: "L",
            0b111111100100100100011000: "P",
            0b111111100100100110011001: "R",
            0b111110000001000001111110: "U",
            0b100011100101101001110001: "Z",
        }.get(k, "?")
        n += 1

    return out


print(part_2())
