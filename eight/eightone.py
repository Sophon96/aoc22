with open("input.txt", "r") as ifp:
    lines = tuple(map(str.strip, ifp.readlines()))

visible = [[False] * len(lines[0]) for _ in range(len(lines))]
tmax = [-1] * len(lines[0])
for i, line in enumerate(lines):
    lmax = -1
    for i2, c in enumerate(line):
        c = int(c)
        if c > lmax:
            lmax = c
            visible[i][i2] = True

        if c > tmax[i2]:
            tmax[i2] = c
            visible[i][i2] = True

    rmax = -1
    for i2, c in enumerate(reversed(line)):
        c = int(c)
        if c > rmax:
            rmax = c
            visible[i][len(line) - 1 - i2] = True

bmax = [-1] * len(lines[0])
for i, line in enumerate(reversed(lines)):
    for i2, c in enumerate(line):
        c = int(c)
        if c > bmax[i2]:
            bmax[i2] = c
            visible[len(lines) - 1 - i][i2] = True

print(sum(sum(line) for line in visible))
