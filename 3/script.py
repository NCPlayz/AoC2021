from typing import Counter


x = []
data = [d.strip() for d in open("./3/input.txt").readlines()]
for line in data:
    for i in range(len(line)):
        if len(x) < len(line):
            x.append("")
        x[i] += line[i]


y = [Counter(_) for _ in x]

gamma = ""
epsilon = ""

for c in y:
    gamma += c.most_common(1)[0][0]
    epsilon += c.most_common()[-1][0]

print("Part 1", int(gamma, 2) * int(epsilon, 2))


def get_gas(data, *, inverted=False):
    for i in range(len(x)):
        count = 0
        for line in data:
            count += {"0": 1, "1": -1}[line[i]]

        if count > 0:
            data = [line for line in data if line[i] == ("1" if inverted else "0")]
        else:
            data = [line for line in data if line[i] == ("0" if inverted else "1")]

        if len(data) == 1:
            return data[0]


co2 = int(get_gas(data, inverted=True), 2)
oxygen = int(get_gas(data), 2)
print("Part 2", oxygen * co2)
