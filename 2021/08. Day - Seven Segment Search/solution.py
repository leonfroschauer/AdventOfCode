with open("input.txt") as file:
    plines = file.read().strip().splitlines()


def part_1():
    amount = 0
    for line in plines:
        amount += sum(1 for digit in line.split("|")[1].split(" ") if len(digit) in [2, 3, 4, 7])
    return amount


print(part_1())


def part_2():
    out = 0
    for left, right in [line.split('|') for line in plines]:
        # Parse Input
        segments = {}
        for segment in left.split():
            segments[len(segment)] = set(segment)

        numbers = []
        for segment in right.split():
            segment = set(segment)
            if len(segment) == 2:
                numbers.append("1")
            elif len(segment) == 5:
                if len(segment & segments[4]) == 2:
                    numbers.append("2")
                elif len(segment & segments[4]) == 3:
                    if len(segment & segments[2]) == 2:
                        numbers.append("3")
                    elif len(segment & segments[2]) == 1:
                        numbers.append("5")
            elif len(segment) == 6:
                if len(segment & segments[4]) == 4:
                    numbers.append("9")
                elif len(segment & segments[4]) == 3:
                    if len(segment & segments[2]) == 1:
                        numbers.append("6")
                    elif len(segment & segments[2]) == 2:
                        numbers.append("0")
            elif len(segment) == 4:
                numbers.append("4")
            elif len(segment) == 3:
                numbers.append("7")
            elif len(segment) == 7:
                numbers.append("8")
        out += int("".join(numbers))
    return out


print(part_2())
