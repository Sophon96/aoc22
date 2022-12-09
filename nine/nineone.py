ifp = open("input.txt", "r")

directions = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}
visited = {(0, 0)}
tpos, hpos = [0, 0], [0, 0]
for line in ifp:
    direction = directions[line.split()[0]]
    steps = int(line.strip().split()[1])
    for i in range(steps):
        hpos[0] += direction[0]
        hpos[1] += direction[1]

        if abs(hpos[0] - tpos[0]) <= 1 and abs(hpos[1] - tpos[1]) <= 1: continue
        tpos[0] += abs(hpos[0] - tpos[0]) // ((hpos[0] - tpos[0]) or 1)
        tpos[1] += abs(hpos[1] - tpos[1]) // ((hpos[1] - tpos[1]) or 1)
        visited.add(tuple(tpos))

print(len(visited))
