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

lowest = max(filled, key=lambda x: x[1])[1]

fell = 0
can_fall = True
while can_fall:
    pos = (500, 0)
    while True:
        # to the abyss
        if pos[1] > lowest:
            can_fall = False
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
