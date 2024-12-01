import re

# infile = "sample_in.txt"
infile = "input.txt"

regex = re.compile("\s*(\d+)\s*(\d+)")

with open(infile, 'r') as ifp:
    left = []
    right = []
    for line in ifp.readlines():
        line = line.strip()
        match = regex.match(line)
        left.append(match.group(1))
        right.append(match.group(2))
        print(match.groups())
    sleft = sorted(left)
    sright = sorted(right)
    mapright = { x: sright.count(x) for x in sright }
    delta = 0
    for index in range(0, len(sleft)):
        delta += int(sleft[index]) * int(mapright.get(sleft[index], 0))
        print(delta)
    print("---")
    print(delta)

print("Done!")