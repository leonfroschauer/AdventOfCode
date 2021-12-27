with open("input.txt") as file:
    plines = file.read().strip().splitlines()


def part_1():
    seen, answer = set(), set()
    for order in plines:
        x1, y1, x2, y2 = map(int, order.split(" -> ")[0].split(",") + order.split(" -> ")[1].split(","))
        if y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                if (x, y1) in seen:
                    answer.add((x, y1))
                seen.add((x, y1))
        elif x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                if (x1, y) in seen:
                    answer.add((x1, y))
                seen.add((x1, y))
    return len(answer)


print(part_1())


def part_2():
    seen, answer = set(), set()
    for order in plines:
        x1, y1, x2, y2 = map(int, order.split(" -> ")[0].split(",") + order.split(" -> ")[1].split(","))
        if y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                if (x, y1) in seen:
                    answer.add((x, y1))
                seen.add((x, y1))
        elif x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                if (x1, y) in seen:
                    answer.add((x1, y))
                seen.add((x1, y))
        else:
            range_ = lambda i, j: range(i, j + 1) or range(i, j - 1, -1)
            for x, y in zip(range_(x1, x2), range_(y1, y2)):
                if (x, y) in seen:
                    answer.add((x, y))
                seen.add((x, y))
    return len(answer)


print(part_2())
