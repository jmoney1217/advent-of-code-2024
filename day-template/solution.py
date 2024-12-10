import re

def readinput():
    infile = "sample_in.txt"
    # infile = "input.txt"
    with open(infile, 'r') as ifp:
        lines = [ line.strip() for line in ifp.readlines() ]
    return lines        

def part1(lines):
    answer = 0
    for line in lines:
        pass
    print("---")
    print(answer)

def part2(lines):
    answer = 0
    for line in lines:
        pass
    print("---")
    print(answer)

def main():
    lines = readinput()
    part1(lines)
    part2(lines)

if __name__=="__main__":
    main()
