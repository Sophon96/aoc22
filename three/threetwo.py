import string

ifp = open("input.txt", "r")
imap = (0,) + tuple(string.ascii_letters)

net_prio = 0
current_line = 0
current_intersect = set(string.ascii_letters)
for line in ifp:
    current_line += 1
    current_line %= 3
    current_intersect.intersection_update(set(line.strip()))

    if current_line == 0:
        net_prio += imap.index(current_intersect.pop())
        current_intersect = set(string.ascii_letters)

ifp.close()
print(net_prio)
