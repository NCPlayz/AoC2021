from collections import defaultdict

_map: defaultdict[defaultdict[int]] = defaultdict(lambda: defaultdict(int))
# [x][y]
part_1 = 0  # i don't remember how i got part 1 to work but i think it's correct
part_2 = 0

data = open("./5/input.txt").read().splitlines()

for line in data:
    coords = line.replace(" ", "").split("->")
    x, y = coords[0].split(",")
    original_x, original_y = int(x), int(y)
    x, y = int(x), int(y)
    x2, y2 = coords[1].split(",")
    x2, y2 = int(x2), int(y2)

    x_diff = abs(x2 - x)
    y_diff = -abs(y2 - y)

    x_step = 1 if x < x2 else -1
    y_step = 1 if y < y2 else -1
    err = x_diff + y_diff

    while True:
        _map[x][y] += 1
        if _map[x][y] == 2:
            part_2 += 1
        if x == x2 and y == y2:
            break
        e2 = 2 * err

        if e2 > y_diff:
            err += y_diff
            x += x_step
        if e2 < x_diff:
            err += x_diff
            y += y_step

print("Part 1", part_1)
print("Part 2", part_2)
