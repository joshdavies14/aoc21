f = open("in.txt", "r")

x, y, aim = 0, 0, 0

for line in f:
    command = line.split(" ")[0]
    distance = int(line.split(" ")[1])
    if command == "forward":
        x += distance
        y += (distance * aim)
    elif command == "up":
        aim -= distance
    elif command == "down":
        aim += distance

print(x * y)