import re


ifp = open("input.txt", "r")

xs = [
    1,
]
sc = 0
for line in ifp:
    if a := re.findall(r"addx (\-?\d+)", line):
        xs.extend([xs[-1], xs[-1] + int(a[0])])
        continue
    xs.append(xs[-1])

# did not reach 179
if len(xs) < 220:
    xs.extend([xs[-1]] * (220 - len(xs)))

ifp.close()

for i in range(len(xs)):
    if i % 40 == 0:
        print()
    print(".#"[(i % 40) in {xs[i] - 1, xs[i], xs[i] + 1}], end="")
