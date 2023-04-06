with open("input.txt") as file:
    puzzle = open("input.txt").read().strip()
    crabs = sorted(list(map(int, puzzle.split(","))))


def part_1():
    median = crabs[len(crabs) // 2]
    return sum(abs(crab - median) for crab in crabs)


print(part_1())


def part_2():
    mean = sum(crabs) // len(crabs)
    return int(sum((score := abs(crab - mean)) * (0.5 * score + 0.5) for crab in crabs))


print(part_2())
