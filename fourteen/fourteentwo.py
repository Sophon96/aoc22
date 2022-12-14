import re

filled: set[tuple[int, int]] = set()

with open("input.txt", "r") as ifp:
    for line in ifp:
        coords = re.findall(r"(\d+),(\d+)", line)
        for i in range(len(coords) - 1):
            x1, y1 = map(int, coords[i])
            x2, y2 = map(int, coords[i + 1])
            if x1 == x2:
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    filled.add((x1, y))
            else:
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    filled.add((x, y1))

floor = max(filled, key=lambda x: x[1])[1] + 2

fell = 0
while (500, 0) not in filled:
    pos = (500, 0)
    while True:
        # hit the floor
        if pos[1] + 1 == floor:
            filled.add(pos)
            fell += 1
            break

        # down
        next_pos = (pos[0], pos[1] + 1)
        if next_pos not in filled:
            pos = next_pos
            continue

        # left
        next_pos = (pos[0] - 1, pos[1] + 1)
        if next_pos not in filled:
            pos = next_pos
            continue

        # right
        next_pos = (pos[0] + 1, pos[1] + 1)
        if next_pos not in filled:
            pos = next_pos
            continue

        # down, left, right, no dice
        filled.add(pos)
        fell += 1
        break

print(fell)
