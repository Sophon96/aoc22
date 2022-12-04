import re

ifp = open("input.txt", "r")

overlaps = 0
for line in ifp:
    bounds = tuple(map(int, re.findall(r"(\d+)", line)))
    overlaps += bool(
        set(range(bounds[0], bounds[1] + 1)) & set(range(bounds[2], bounds[3] + 1))
    )

ifp.close()
print(overlaps)
