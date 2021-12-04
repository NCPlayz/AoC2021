class C(int):
    chosen = False


data = open("./4/input.txt").read().splitlines().__add__([""])

numbers = [int(x) for x in data[0].split(",")]

boards, b = [], []
for line in data[2:]:
    if line:
        b.append([C(d) for d in line.split() if d != ""])
    else:
        boards.append(b)
        b = []


def check_win(board):
    for row in board:
        if all(c.chosen for c in row):
            return True

    for col in range(len(board[0])):
        if all(board[i][col].chosen for i in range(len(board))):
            return True
    return False


ignore = []
for n in numbers:
    for b in boards:
        for r in b:
            for c in r:
                c.chosen |= c == n

        if check_win(b) and b not in ignore:
            ignore.append(b)
            score = sum(sum(c for c in r if not c.chosen) for r in b) * n

            if len(ignore) == 1:
                print("Part 1", score)

            if len(ignore) == len(boards):
                print("Part 2", score)
                exit()
