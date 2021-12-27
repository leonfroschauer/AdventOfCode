with open("input.txt") as file:
    plines = file.read().strip().splitlines()


def part_1():
    depth, horizontal = 0, 0
    for order in plines:
        order = order.split()[0], int(order.split()[1])
        if order[0] == "forward":
            horizontal += order[1]
        elif order[0] == "down":
            depth += order[1]
        else:
            depth -= order[1]
    return depth * horizontal


print(part_1())


def part_2():
    depth, horizontal, aim = 0, 0, 0
    for order in plines:
        order = order.split()[0], int(order.split()[1])
        if order[0] == "down":
            aim += order[1]
        elif order[0] == "up":
            aim -= order[1]
        else:
            horizontal += order[1]
            depth += aim * order[1]
    return depth * horizontal


print(part_2())
