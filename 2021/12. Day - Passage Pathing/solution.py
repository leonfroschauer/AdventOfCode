from collections import defaultdict


plines = open("input.txt").read().strip().splitlines()


def part_1():
    graph = defaultdict(list)
    for line in plines:
        start, end = line.split("-")
        graph[start].append(end)
        graph[end].append(start)

    def find_in_path(node: str, seen: list) -> int:
        if node == "end":
            return 1
        if node in seen and node.islower():
            return 0
        return sum(find_in_path(new_node, seen + [node]) for new_node in graph[node])

    return find_in_path("start", [])


print(part_1())


def part_2():
    graph = defaultdict(list)
    for line in plines:
        start, end = line.split("-")
        graph[start].append(end)
        graph[end].append(start)

    def find_in_path(node: str, seen: list, twice: bool) -> int:
        if node == "end":
            return 1
        if node in seen:
            if node == "start":
                return 0
            if node.islower():
                if twice:
                    return 0
                twice = True
        return sum(find_in_path(new_node, seen + [node], twice) for new_node in graph[node])

    return find_in_path("start", [], False)


print(part_2())
