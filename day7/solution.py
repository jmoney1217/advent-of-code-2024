import re, sys, copy
from collections import defaultdict

regex = re.compile("(\d+): (.*)")

def readinput():
    # infile = "sample_in.txt"
    infile = "input.txt"
    with open(infile, 'r') as ifp:
        lines = [ line.strip() for line in ifp.readlines() ]
    return lines        

def recursiveAddMult(solution, left, rights):
    right = rights[0]
    lefts = [left + right, left * right]
    
    if len(rights) > 1:
        for newleft in lefts:
            if recursiveAddMult(solution, newleft, rights[1:]):
                return True
        return False
    else:
        if solution in lefts:
            return True
        else:
            return False
        
def recursiveAddMultCat(solution, left, rights):
    right = rights[0]
    lefts = [left + right, left * right, int("{}{}".format(left, right))]
    
    if len(rights) > 1:
        for newleft in lefts:
            if recursiveAddMultCat(solution, newleft, rights[1:]):
                return True
        return False
    else:
        if solution in lefts:
            return True
        else:
            return False


def part1(lines):
    answer = 0

    for line in lines:
        groups = regex.match(line).groups()
        solution = int(groups[0])
        vals = [ int(x) for x in groups[1].split() ]
        left = vals[0]
        rights = vals[1:]
        if recursiveAddMult(solution, left, rights):
            answer += solution
            # print("SUCCESS: {}".format(line))
        else:
            # print("FAIL   : {}".format(line))
            pass

    print("---")
    print(answer)

    # Part 2
    answer = 0
    
    for line in lines:
        groups = regex.match(line).groups()
        solution = int(groups[0])
        vals = [ int(x) for x in groups[1].split() ]
        left = vals[0]
        rights = vals[1:]
        if recursiveAddMultCat(solution, left, rights):
            answer += solution
            # print("SUCCESS: {}".format(line))
        else:
            # print("FAIL   : {}".format(line))
            pass

    print("---")
    print(answer)

def main():
    lines = readinput()
    part1(lines)

if __name__=="__main__":
    main()
