y = [int(line) for line in open("./1/input.txt").read().splitlines()]

previous_measurement = None
increases = 0

for measurement in y:
    if previous_measurement is not None:
        increases += measurement > previous_measurement
    previous_measurement = measurement

print("Part 1", increases)

groups = [sum(y[i : i + 3]) for i in range(0, len(y) - 2)]

previous_measurement = None
count = 0

for measurement in groups:
    if previous_measurement is not None:
        count += measurement > previous_measurement
    previous_measurement = measurement

print("Part 2", count)
