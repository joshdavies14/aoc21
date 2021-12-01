f = open("in.txt", "r")

total = 0
temp = 0

for line in f:
    if int(line) > temp:
        total += 1
    temp = int(line)

print(total - 1)