f = open("in.txt", "r")
lines = f.readlines()
lines = [line.rstrip() for line in lines]
length = len(lines[0])

sumposition = [0] * length
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

o2result = lines.copy()
cresult = lines.copy()

for x in range(length):
    if len(o2result) > 1:
        o2count = 0
        for o2line in o2result:
            if o2line[x] == "1":
                o2count += 1
        o2mid = len(o2result)/2
        if o2count >= o2mid:
            o2target = "1"
        else:
            o2target = "0"
        o2result = [a for a in o2result if a[x] == o2target]
    if len(cresult) > 1:
        ccount = 0
        for cline in cresult:
            if cline[x] == "1":
                ccount += 1
        cmid = len(cresult)/2
        if ccount >= cmid:
            ctarget = "0"
        else:
            ctarget = "1"
        cresult = [a for a in cresult if a[x] == ctarget]

o2num = int(o2result[0], 2)
cnum = int(cresult[0], 2)

print(o2num * cnum)

