import re, sys
from collections import defaultdict

def readinput():
    # infile = "sample_in.txt"
    infile = "input.txt"
    with open(infile, 'r') as ifp:
        lines = [ line.strip() for line in ifp.readlines() ]
    return lines        

def part1(lines):
    answer = 0
    rules = defaultdict(list)
    updates = []
    for line in lines:
        if '|' in line:
            parts = line.split('|')
            rules[int(parts[0])].append(int(parts[1]))
        elif line:
            updates.append([int(x) for x in line.split(',')])
    invalids = []
    for update in updates:
        lpages=[]
        valid = True
        for cpage in update:
            for page in lpages:
                # print("Page: {} Rules: {}".format(page, rules[cpage]))
                if page in rules[cpage]:
                    valid = False
                    break
            if not valid:
                break
            lpages.append(cpage)
        if valid:
            # print("Valid:   {}".format(update))
            answer += update[int(len(update)/2)]
        else:
            # print("Invalid: {}".format(update))
            invalids.append(update)

    print("---")
    print(answer)

    # Part 2
    answer = 0
    for invalid in invalids:
        valid = False
        while not valid:
            lpages=[]
            valid = True
            for ci, cpage in enumerate(invalid):
                for li, lpage in enumerate(lpages):
                    # print("CPage: {} LPage: {} Rules: {}".format(cpage, lpage, rules[cpage]))
                    if lpage in rules[cpage]:
                        valid = False
                        invalid = lpages[0:li]+[cpage]+lpages[li:]+invalid[ci+1:]
                        break
                if not valid:
                    break
                lpages.append(cpage)
            if valid:
                # print("Valid:   {}".format(invalid))
                answer += invalid[int(len(invalid)/2)]
            # else:
                # print("Still Invalid: {}".format(invalid))

    print("---")
    print(answer)

def main():
    lines = readinput()
    part1(lines)

if __name__=="__main__":
    main()
