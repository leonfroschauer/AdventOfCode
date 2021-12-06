puzzle = open("input.txt").read().strip()


def part_1():
    """Function to solve the first part of the AoC puzzle"""
    fish = [puzzle.count(str(i)) for i in range(9)]
    for j in range(80):
        fish.append(zeros := fish.pop(0))
        fish[6] += zeros
    return sum(fish)


print(part_1())


def part_2():
    """Function to solve the second part of the AoC puzzle"""
    fish = [puzzle.count(str(i)) for i in range(9)]
    for j in range(256):
        fish.append(zeros := fish.pop(0))
        fish[6] += zeros
    return sum(fish)


print(part_2())
