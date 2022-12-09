ifp = open("input.txt", "r")

directions = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}
visited = {(0, 0)}
poss = [[0, 0] for _ in range(10)]
for line in ifp:
    direction = directions[line.split()[0]]
    steps = int(line.strip().split()[1])
    for i in range(steps):
        poss[0][0] += direction[0]
        poss[0][1] += direction[1]

        for i2 in range(1, 10):
            if abs(poss[i2-1][0] - poss[i2][0]) <= 1 and abs(poss[i2-1][1] - poss[i2][1]) <= 1: continue
            poss[i2][0] += abs(poss[i2-1][0] - poss[i2][0]) // ((poss[i2-1][0] - poss[i2][0]) or 1)
            poss[i2][1] += abs(poss[i2-1][1] - poss[i2][1]) // ((poss[i2-1][1] - poss[i2][1]) or 1)
        visited.add(tuple(poss[9]))

print(len(visited))
