from queue import PriorityQueue

with open("input.txt", "r") as ifp:
    inp = tuple(map(tuple, map(str.strip, ifp.readlines())))
    hm = (
        [[chr(250)] * (len(inp[0]) + 2)]
        + [[chr(250), *row, chr(250)] for row in inp]
        + [[chr(250)] * (len(inp[0]) + 2)]
    )

s = None
for i, row in enumerate(hm):
    for i2, c in enumerate(row):
        if c == "S":
            s = (i, i2)
            break
    if s is not None:
        break
assert s is not None

seen = set()
pq = PriorityQueue()
for direction in ((-1, 0), (1, 0), (0, -1), (0, 1)):
    if ord(hm[s[0] + direction[0]][s[1] + direction[1]]) - ord('a') <= 1:
        seen.add((s[0] + direction[0], s[1] + direction[1]))
        pq.put((1, (s[0] + direction[0], s[1] + direction[1])))

while not pq.empty():
    c, p = pq.get()
    if hm[p[0]][p[1]] == "E":
        print(c)
        break
    for direction in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        if (
            ord(v if (v := hm[p[0] + direction[0]][p[1] + direction[1]]) != 'E' else 'z') - ord(hm[p[0]][p[1]]) <= 1
            and (p[0] + direction[0], p[1] + direction[1]) not in seen
        ):
            seen.add((p[0] + direction[0], p[1] + direction[1]))
            pq.put((c + 1, (p[0] + direction[0], p[1] + direction[1])))
