plines = open("input.txt").read().strip().splitlines()


def part_1():
    gamma_rate = ""
    for numbers in zip(*plines):
        gamma_rate += "1" if numbers.count("1") > numbers.count("0") else "0"
    return int(gamma_rate, 2) * (int(gamma_rate, 2) ^ int("111111111111", 2))  # XOR operation


print(part_1())


def part_2():

    def calculate_rating(numbers: list, oxygen_generator: bool, i: int = 0):
        count_zero, count_one = 0, 0
        for number in numbers:
            if number[i] == "1":
                count_one += 1
            else:
                count_zero += 1
        # Determine if the least or most common should be counted
        if (oxygen_generator and count_one >= count_zero) or (not oxygen_generator and count_zero > count_one):
            numbers = [number for number in numbers if number[i] == "1"]
        else:
            numbers = [number for number in numbers if number[i] == "0"]
        return int(numbers[0], 2) if len(numbers) == 1 else calculate_rating(numbers, oxygen_generator, i + 1)
    return calculate_rating(plines, True) * calculate_rating(plines, False)


print(part_2())
