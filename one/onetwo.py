ifp = open('input.txt', 'r')

top3 = [0, 0, 0]
current_sum = 0
for line in ifp:
    if line == '\n':
        if current_sum > top3[2]:
            top3[2] = current_sum
            top3.sort(reverse=True)

        current_sum = 0
        continue

    cal = int(line.strip())
    current_sum += cal

print(sum(top3))
ifp.close()
