with open("input.txt") as file:
    octopuses = {(x, y): int(elm) for y, row in enumerate(file) for x, elm in enumerate(row.strip())}


def part_1():
    total_flashes = 0
    octopuses_ = octopuses.copy()

    for _ in range(100):
        flashes = set()
        for key in octopuses_:
            octopuses_[key] += 1
            if octopuses_[key] > 9:
                flashes.add(key)

        while flashes:
            x, y = flashes.pop()
            octopuses_[x, y] = 0
            total_flashes += 1
            for neighbour in filter(octopuses_.get, [(x + dx, y + dy) for dx in [1, 0, -1] for dy in [1, 0, -1]]):
                octopuses_[neighbour] += 1
                if octopuses_[neighbour] > 9:
                    flashes.add(neighbour)
    return total_flashes


print(part_1())


def part_2():
    steps = 0

    while True:
        steps += 1
        flashes = set()
        for key in octopuses:
            octopuses[key] += 1
            if octopuses[key] > 9:
                flashes.add(key)

        while flashes:
            x, y = flashes.pop()
            octopuses[x, y] = 0
            for neighbour in filter(octopuses.get, [(x + dx, y + dy) for dx in [1, 0, -1] for dy in [1, 0, -1]]):
                octopuses[neighbour] += 1
                if octopuses[neighbour] > 9:
                    flashes.add(neighbour)

        if sum(octopuses.values()) == 0:
            return steps


print(part_2())
