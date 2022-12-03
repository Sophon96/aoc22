import string

ifp = open('input.txt', 'r')
imap = (0,) + tuple(string.ascii_letters)

net_prio = 0
for line in ifp:
    c1, c2 = set(line.strip()[:len(line.strip())//2]), set(line.strip()[len(line.strip())//2:])
    net_prio += imap.index(c1.intersection(c2).pop())

print(net_prio)
