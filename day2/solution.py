import copy

def readinput():
    # infile = "sample_in.txt"
    infile = "input.txt"
    with open(infile, 'r') as ifp:
        lines = [ line.strip() for line in ifp.readlines() ]
    return lines        

def part1(lines):
    answer = 0
    for line in lines:
        levels = [int(x) for x in line.split()]
        slevels = sorted(levels)
        rslevels = list(reversed(slevels))
        if levels not in (slevels, rslevels):
            # print("Bad 1: {}".format(levels))
            continue
        ok=True
        for x in range(0, len(levels)-1):
            delta = abs(levels[x+1]-levels[x])
            if not 1 <= delta <= 3:
                # print("Bad 2: {}".format(levels))
                ok=False
                break
        if ok:
            answer += 1
            # print("Good: {}".format(levels))

    print("Part 1: {}".format(answer))

def part2(lines):
    answer = 0
    for line in lines:
        levels = [int(x) for x in line.split()]
        ok=False
        removeIndex=-1
        while not ok and removeIndex < len(levels):
            check=copy.deepcopy(levels)
            if removeIndex >= 0:
                del(check[removeIndex])
            slevels = sorted(check)
            rslevels = list(reversed(slevels))
            if check not in (slevels, rslevels):
                # print("Bad 1: {}".format(check))
                removeIndex+=1
                continue

            dok=True
            for x in range(0, len(check)-1):
                delta = abs(check[x+1]-check[x])
                if not 1 <= delta <= 3:
                    # print("Bad 2: {}".format(check))
                    dok=False
                    break
            if dok:
                answer += 1
                # print("Good: {}".format(levels))
                ok=True
            else:
                removeIndex+=1
            
    print("Part 2: {}".format(answer))
            
def main():
    lines = readinput()
    part1(lines)
    part2(lines)

if __name__=="__main__":
    main()
