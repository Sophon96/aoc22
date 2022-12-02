ifp = open('input.txt', 'r')
score = 0
play_map = {
    # self first
    'X': {
        'A': 3 + 1,
        'B': 0 + 1,
        'C': 6 + 1,
    },
    'Y': {
        'A': 6 + 2,
        'B': 3 + 2,
        'C': 0 + 2,
    },
    'Z': {
        'A': 0 + 3,
        'B': 6 + 3,
        'C': 3 + 3,
    },
}

for line in ifp:
    opp, slf = line.split()
    score += play_map[slf][opp]

ifp.close()
print(score)
