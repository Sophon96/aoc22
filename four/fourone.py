import re

ifp = open("input.txt", "r")

overlaps = 0
for line in ifp:
    bounds = tuple(map(int, re.findall(r"(\d+)", line)))
    overlaps += (
        bounds[0] == bounds[2]
        or bounds[1] == bounds[3]
        or ((bounds[0] > bounds[2]) == (bounds[1] < bounds[3]))
    )

ifp.close()
print(overlaps)
