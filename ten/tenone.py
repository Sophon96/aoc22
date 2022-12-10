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

print(
    xs[19] * 20
    + xs[59] * 60
    + xs[99] * 100
    + xs[139] * 140
    + xs[179] * 180
    + xs[219] * 220
)
