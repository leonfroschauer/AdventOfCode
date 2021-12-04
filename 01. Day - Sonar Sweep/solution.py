puzzle = open("input.txt").read().strip()
plines = puzzle.splitlines()
plines = list(map(int, plines))


def part_1():
    result = 0
    for x, y in zip(plines, plines[1:]):
        if y > x:
            result += 1
    return result


print(part_1())


def part_2():
    result = 0
    for x, y in zip(plines, plines[3:]):
        if y > x:
            result += 1
    return result


print(part_2())
