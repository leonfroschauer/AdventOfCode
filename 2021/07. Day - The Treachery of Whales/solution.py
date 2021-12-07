crabs = sorted(list(map(int, open("input.txt").read().strip().split(","))))


def part_1():
    median = crabs[len(crabs)//2]
    return sum(abs(crab - median) for crab in crabs)


print(part_1())


def part_2():
    mean = sum(crabs) // len(crabs)
    return sum((score := abs(crab - mean)) * (0.5 * score + 0.5) for crab in crabs)


print(part_2())
