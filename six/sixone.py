with open("input.txt", "r") as ifp:
    packet = ifp.readline().strip()

sequence = list(packet[:3])
for i, character in tuple(enumerate(packet))[3:]:
    sequence.append(character)
    if len(set(sequence)) < 4:
        sequence.pop(0)
    else:
        print(i+1)
        break
