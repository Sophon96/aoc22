from queue import PriorityQueue

with open("input.txt", "r") as ifp:
    inp = tuple(map(tuple, map(str.strip, ifp.readlines())))
    hm = (
        [[chr(0)] * (len(inp[0]) + 2)]
        + [[chr(0), *row, chr(0)] for row in inp]
        + [[chr(0)] * (len(inp[0]) + 2)]
    )

e = None
for i, row in enumerate(hm):
    for i2, c in enumerate(row):
        if c == "E":
            e = (i, i2)
            break
    if e is not None:
        break
assert e is not None

seen = set()
pq = PriorityQueue()
for direction in ((-1, 0), (1, 0), (0, -1), (0, 1)):
    if ord("z") - ord(hm[e[0] + direction[0]][e[1] + direction[1]]) <= 1:
        seen.add((e[0] + direction[0], e[1] + direction[1]))
        pq.put((1, (e[0] + direction[0], e[1] + direction[1])))

while not pq.empty():
    c, p = pq.get()
    if hm[p[0]][p[1]] == "a":
        print(c)
        break
    for direction in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        if (
            ord(hm[p[0]][p[1]])
            - ord(
                v
                if (v := hm[p[0] + direction[0]][p[1] + direction[1]]) not in ("S", "E")
                else {"E": "z", "S": "a"}[v]
            )
            <= 1
            and (p[0] + direction[0], p[1] + direction[1]) not in seen
        ):
            seen.add((p[0] + direction[0], p[1] + direction[1]))
            pq.put((c + 1, (p[0] + direction[0], p[1] + direction[1])))
