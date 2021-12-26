with open("input.txt") as file:
    plines = file.read().strip().splitlines()


def part_1():
    counter = {bracket: 0 for bracket in ")]}>"}
    for line in plines:
        opened = []
        for char in line:
            if char in "([{<":
                opened.append(char)
            else:
                if opened.pop(-1) + char not in ["()", "[]", "{}", "<>"]:
                    counter[char] += 1
                    break
    return counter[")"] * 3 + counter["]"] * 57 + counter["}"] * 1197 + counter[">"] * 25137


print(part_1())


def part_2():
    scores = []
    for line in plines:
        opened = []
        for char in line:
            if char in "([{<":
                opened.append(char)
            else:
                if opened.pop(-1) + char not in ["()", "[]", "{}", "<>"]:
                    break
        else:
            score = 0
            for char in opened[::-1]:
                score = score * 5 + {"(": 1, "[": 2, "{": 3, "<": 4}[char]
            scores.append(score)
    scores.sort()
    return scores[len(scores) // 2]


print(part_2())
