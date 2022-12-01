ifp = open('input.txt', 'r')

running_max = -1
current_sum = 0
for line in ifp:
    if line == '\n':
        running_max = max(current_sum, running_max)
        current_sum = 0
        continue

    cal = int(line.strip())
    current_sum += cal

print(running_max)
ifp.close()
