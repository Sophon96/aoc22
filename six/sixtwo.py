with open("input.txt", "r") as ifp:
    packet = ifp.readline().strip()

sequence = list(packet[:13])
for i, character in tuple(enumerate(packet))[13:]:
    sequence.append(character)
    if len(set(sequence)) < 14:
        sequence.pop(0)
    else:
        print(i+1)
        break
