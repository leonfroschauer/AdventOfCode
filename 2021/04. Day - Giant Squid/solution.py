with open("input.txt") as file:
    plines = file.read().strip().splitlines()


def part_1():
    draws = list(map(int, plines[0].split(",")))
    boards = [list(map(int, board.split())) for board in open("input.txt").read().split('\n\n')[1:]]
    boards = [[board[i:i + 5] for i in range(0, 24, 5)] for board in boards]
    watched = []  # Store which numbers were drawn

    def check_winner(board: list) -> bool:
        for i in range(5):
            if all(board[i][j] in watched for j in range(5)) or all(board[j][i] in watched for j in range(5)):
                return True
        return False

    score = lambda board_, draw: sum(num for line in board_ for num in line if num not in watched) * draw

    for number in draws:
        watched.append(number)
        for i, board in enumerate(boards):
            if check_winner(board):
                return score(board, number)


print(part_1())


def part_2():
    draws = list(map(int, plines[0].split(",")))
    boards = [list(map(int, board.split())) for board in open("input.txt").read().split('\n\n')[1:]]
    boards = [[board[i:i + 5] for i in range(0, 24, 5)] for board in boards]
    watched = []  # Store which numbers were drawn
    length, count = len(boards), 0

    def check_winner(board: list) -> bool:
        for i in range(5):
            if all(board[i][j] in watched for j in range(5)) or all(board[j][i] in watched for j in range(5)):
                return True
        return False

    score = lambda board_, draw: sum(num for line in board_ for num in line if num not in watched) * draw

    for number in draws:
        new_boards = []
        watched.append(number)
        for i, board in enumerate(boards):
            if check_winner(board):
                count += 1
                if count == length:
                    return score(board, number)
            else:
                new_boards.append(board)
        boards = new_boards


print(part_2())
