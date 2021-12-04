x, y = 0, 0
y2, aim = 0, 0

data = open("./2/input.txt").read().splitlines()

for line in data:
    move, distance = line.strip().split()
    distance = int(distance)

    if move == "down":
        y += distance

        aim += distance
    elif move == "up":
        y -= distance

        aim -= distance
    elif move == "forward":
        x += distance

        y2 += aim * distance


print("Part 1", x * y)
print("Part 2", x * y2)
