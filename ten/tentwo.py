import re


ifp = open("input.txt", "r")

xs = [
    1,
]
sc = 0
pos = 0
for line in ifp:
    print(".#"[pos in {xs[-1] - 1, xs[-1], xs[-1] + 1}], end="")
    pos = (pos + 1) % 40
    if pos == 0:
        print()

    if a := re.findall(r"addx (\-?\d+)", line):
        val = xs[-1] + int(a[0])
        print(".#"[pos in {xs[-1] - 1, xs[-1], xs[-1] + 1}], end="")    # got this after contest
        pos = (pos + 1) % 40
        if pos == 0:
            print()
        xs.extend([xs[-1], val])
        continue
    xs.append(xs[-1])

ifp.close()
