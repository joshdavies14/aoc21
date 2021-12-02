f = open("in.txt", "r")

x, y = 0, 0

for line in f:
    command = line.split(" ")[0]
    distance = int(line.split(" ")[1])
    if command == "forward":
        x += distance
    elif command == "up":
        y -= distance
    elif command == "down":
        y += distance

print(x * y)