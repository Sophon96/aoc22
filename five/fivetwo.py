import re

ifp = open("input.txt", "r")

stacks = None
for line in ifp:
    # handle end of stack section
    if line == '\n':
        # end of stack section
        break
    elif line[1].isdigit():
        # stack numbers (useless)
        continue

    if stacks is None:
        stacks = [[] for _ in range(len(line)//4)]

    # trust me bro
    tuple(e and stacks[i].append(e) for i, e in enumerate(re.findall(r"(?:(?:   |\[([A-Z])\])[ \n])", line)))

stacks = [s[::-1] for s in stacks]

for line in ifp:
    qty, src, dst = map(int, re.findall(r"(\d+)", line))
    src -= 1
    dst -= 1
    stacks[dst].extend(stacks[src][-qty:])
    stacks[src] = stacks[src][:-qty]

ifp.close()
print(''.join((s[-1] for s in stacks)))
