with open("input.txt", "r") as ifp:
    lines = tuple(map(str.strip, ifp.readlines()))

highscore = -1
for i, line in enumerate(lines):
    for i2, c in enumerate(line):
        scores = [0] * 4
        # floodfill up, down, left, right
        for d, dx, dy in ((0, 0, -1), (1, 0, 1), (2, -1, 0), (3, 1, 0)):
            x, y = i, i2
            while True:
                x += dx
                y += dy
                if x < 0 or y < 0 or x >= len(line) or y >= len(lines):
                    break

                scores[d] += 1
                if int(lines[x][y]) >= int(c):
                    break

        if (score := scores[0] * scores[1] * scores[2] * scores[3]) > highscore:
            highscore = score

print(highscore)
