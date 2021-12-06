puzzle = open("input.txt").read().strip()


def part_1():
    fish = [puzzle.count(str(i)) for i in range(9)]
    for j in range(80):
        zeros = fish.pop(0)
        fish.append(zeros)
        fish[6] += zeros
    return sum(fish)


print(part_1())


def part_2():
    fish = [puzzle.count(str(i)) for i in range(9)]
    for j in range(256):
        zeros = fish.pop(0)
        fish.append(zeros)
        fish[6] += zeros
    return sum(fish)


print(part_2())
