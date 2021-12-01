f = open("in.txt", "r")

lines = f.readlines()
lines = [int(line.rstrip()) for line in lines]

total = 0

sums = [sum(lines[x:x+3]) for x in range(len(lines)-2)]

for x in range(1, len(sums)):
    if sums[x] > sums[x-1]:
        total += 1

print(total)