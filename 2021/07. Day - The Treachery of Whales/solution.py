crabs = list(map(int, open("input.txt").read().strip().split(",")))


def part_1():
    changes = lambda number: sum(abs(crab - number) for crab in crabs)
    return min(changes(num) for num in range(max(crabs)))


print(part_1())


def part_2():
    changes = lambda number: sum((score := abs(crab - number)) * (0.5 * score + 0.5)for crab in crabs)
    return int(min(changes(num) for num in range(max(crabs))))


print(part_2())
