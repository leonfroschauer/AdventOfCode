with open("input.txt") as file:
    numbers = list(map(int, file.read().strip().splitlines()))


def part_1():
    return sum(num1 < num2 for num1, num2 in zip(numbers, numbers[1:]))


print(part_1())


def part_2():
    return sum(num1 < num2 for num1, num2 in zip(numbers, numbers[3:]))


print(part_2())
