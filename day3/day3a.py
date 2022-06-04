f = open("in.txt", "r")
lines = f.readlines()
lines = [line.rstrip() for line in lines]

sumposition = [0] * len(lines[0])
mid = len(lines)/2

for line in lines:
    for x in range(len(line)):
        sumposition[x] = sumposition[x] + int(line[x])

gammastring = ""
epsilonstr = ""

for position in sumposition:
    if position > mid:
        gammastring += "1"
        epsilonstr += "0"
    else:
        gammastring += "0"
        epsilonstr += "1"

gamma = int(gammastring, 2)
epsilon = int(epsilonstr, 2)

print(gamma*epsilon)

