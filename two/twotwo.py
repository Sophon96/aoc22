ifp = open("input.txt", "r")
score = 0

for line in ifp:
    opp, slf = line.split()
    score += (ord(slf) - ord("X")) * 3 + (
        (((ord(opp) - ord("A")) + (ord(slf) - ord("Y"))) % 3) + 1
    )

ifp.close()
print(score)
