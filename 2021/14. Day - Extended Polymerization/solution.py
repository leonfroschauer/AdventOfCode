from collections import Counter


with open("input.txt") as file:
    template, _, *rules = open("input.txt").read().split('\n')
    rules = dict(r.split(" -> ") for r in rules)
    pairs = Counter(["".join(pair) for pair in zip(template[0::], template[1::])])
    chars = Counter(template)


def part_1():
    pairs_ = pairs.copy()
    chars_ = chars.copy()
    for _ in range(10):
        for (char_1, char_2), number_in_polymer in pairs_.copy().items():
            pairs_[char_1 + char_2] -= number_in_polymer
            pairs_[char_1 + rules[char_1 + char_2]] += number_in_polymer
            pairs_[rules[char_1 + char_2] + char_2] += number_in_polymer
            chars_[rules[char_1 + char_2]] += number_in_polymer

    return max(chars_.values()) - min(chars_.values())


print(part_1())


def part_2():
    pairs_ = pairs.copy()
    chars_ = chars.copy()
    for _ in range(40):
        for (char_1, char_2), number_in_polymer in pairs_.copy().items():
            pairs_[char_1 + char_2] -= number_in_polymer
            pairs_[char_1 + rules[char_1 + char_2]] += number_in_polymer
            pairs_[rules[char_1 + char_2] + char_2] += number_in_polymer
            chars_[rules[char_1 + char_2]] += number_in_polymer

    return max(chars_.values()) - min(chars_.values())


print(part_2())
