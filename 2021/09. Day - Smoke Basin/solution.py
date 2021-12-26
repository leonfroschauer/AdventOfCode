with open("input.txt") as file:
    cave = {(x, y): int(elm) for y, row in enumerate(file) for x, elm in enumerate(row.strip())}


def part_1():
    neighbours = lambda x, y: [c for c in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)] if c in cave]
    low_points = [key for key in cave.keys() if all(cave[n] > cave[key] for n in neighbours(*key))]
    return sum(cave[key] + 1 for key in low_points)


print(part_1())


def part_2():
    neighbours = lambda x, y: [c for c in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)] if c in cave]
    low_points = [key for key in cave.keys() if all(cave[n] > cave[key] for n in neighbours(*key))]

    def basin_size(coordinate: tuple) -> int:
        if cave[coordinate] == 9:
            return 0
        del cave[coordinate]
        x, y = coordinate
        count = 1
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if (x + dx, y + dy) in cave:
                count += basin_size((x + dx, y + dy))
        return count

    basin = sorted([basin_size(low_point) for low_point in low_points], reverse=True)
    return basin[0] * basin[1] * basin[2]


print(part_2())
