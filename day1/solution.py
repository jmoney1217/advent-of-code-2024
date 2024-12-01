import re

def readinput():
    # infile = "sample_in.txt"
    infile = "input.txt"
    lines = []
    with open(infile, 'r') as ifp:
        for line in ifp.readlines():
            lines.append(line.strip())
    return lines        


def part1(lines):
    regex = re.compile("\s*(\d+)\s*(\d+)")

    left = []
    right = []
    for line in lines:
        match = regex.match(line)
        left.append(match.group(1))
        right.append(match.group(2))
        # print(match.groups())
    sleft = sorted(left)
    sright = sorted(right)
    delta = 0
    for index in range(0, len(sleft)):
        delta += abs(int(sleft[index]) - int(sright[index]))
        # print(delta)
    print("---")
    print(delta)

def part2(lines):
    regex = re.compile("\s*(\d+)\s*(\d+)")

    left = []
    right = []
    for line in lines:
        match = regex.match(line)
        left.append(match.group(1))
        right.append(match.group(2))
        # print(match.groups())
    sleft = sorted(left)
    sright = sorted(right)
    mapright = { x: sright.count(x) for x in sright }
    delta = 0
    for index in range(0, len(sleft)):
        delta += int(sleft[index]) * int(mapright.get(sleft[index], 0))
        # print(delta)
    print("---")
    print(delta)


def main():
    lines = readinput()
    part1(lines)
    part2(lines)

if __name__=="__main__":
    main()
