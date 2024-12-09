import re, sys, copy
from collections import defaultdict

def readinput():
    # infile = "sample_in.txt"
    infile = "input.txt"
    with open(infile, 'r') as ifp:
        lines = [ line.strip() for line in ifp.readlines() ]
    return lines        

def rot90(x, y, direction):
    if x == 1:
        return (0, 1, "S")
    elif x == -1:
        return (0, -1, "N")
    elif y == 1:
        return (-1, 0, "W")
    elif y == -1:
        return (1, 0, "E")
    else:
        print("WTF")
        sys.exit(1)

def part1(lines):
    answer = 1
    data = []
    start_x = 0
    start_y = 0
    offset_x = 0
    offset_y = -1
    direction = "N"
    for li, line in enumerate(lines):
        data.append([])
        for ci, char in enumerate(line):
            data[li].append(char)
            if char == "^":
                start_x = ci
                start_y = li
    
    x = start_x
    y = start_y
    p1data = copy.deepcopy(data)
    steps=0
    while True:
        new_x = x + offset_x
        new_y = y + offset_y
        try:
            new = p1data[new_y][new_x]
        except IndexError:
            print("Leaving area at: [{},{}] offset [{},{}]".format(x, y, offset_x, offset_y))
            break
        if new in ["#", "$"]:
            offset_x, offset_y, direction = rot90(offset_x, offset_y, direction)
            continue
        if new != "X":
            answer += 1
        # else:
        #     print("Duplicate")
        x = new_x
        y = new_y
        p1data[y][x] = "X"
        steps += 1
        if steps > (len(data)*len(data[0])):
            print("We've LOOPED! Abort!")
            sys.exit(1)

    for y in p1data:
        for x in y:
            print(x, end="")
        print()
    
    print("---")
    print(answer)

    sys.exit(0)
    # Part 2
    answer = 0
    for path_y, path_row in enumerate(p1data):
        for path_x, path_pt in enumerate(path_row):
            if path_x == start_x and path_y == start_y:
                continue #starting point is not allowed
                print("^", end="", flush=True)
            if path_pt == "X":
                p2data = copy.deepcopy(data)
                p2data[path_y][path_x] = "$" # new obstacle
                x = start_x
                y = start_y
                p2data[start_x][start_y] = "X" # START
                offset_x = 0
                offset_y = -1
                direction = "N"
                loop_check = defaultdict(lambda: "")
                while True:
                    new_x = x + offset_x
                    new_y = y + offset_y
                    try:
                        new = p2data[new_y][new_x]
                    except IndexError:
                        # print("Leaving area at: [{},{}] offset [{},{}]".format(x, y, offset_x, offset_y))
                        print("-", end="", flush=True)
                        break
                    if new in ["#", "$"]:
                        offset_x, offset_y, direction = rot90(offset_x, offset_y, direction)
                        continue
                    if new != "X":
                        pass
                    elif direction in loop_check[(new_x, new_y)]:
                        print("LOOPING! [{}, {}]".format(path_x, path_y))
                        print("+", end="", flush=True)
                        answer += 1
                        break
                    x = new_x
                    y = new_y
                    p2data[y][x] = "X"
                    loop_check[(x,y)] += direction

    print("---")
    print(answer)

def main():
    lines = readinput()
    part1(lines)

if __name__=="__main__":
    main()
