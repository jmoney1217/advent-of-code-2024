import re

regex = re.compile("(mul\(\d+,\d+\))")
regex2 = re.compile(".*?(\d+),(\d+).*")
regex3 = re.compile("((?:do\(\))|(?:don't\(\))|(?:mul\(\d+,\d+\)))")

def readinput():
    # infile = "sample_in.txt"
    # infile = "sample_in2.txt"
    infile = "input.txt"
    with open(infile, 'r') as ifp:
        lines = [ line.strip() for line in ifp.readlines() ]
    return lines        

def part1(lines):
    answer = 0
    for line in lines:
        for found in regex.findall(line):
            nums = regex2.match(found).groups()
            answer += int(nums[0])*int(nums[1])
    print("---")
    print(answer)

def part2(lines):
    answer = 0
    enabled = True
    for line in lines:
        for found in regex3.findall(line):
            print(found)
            if found == "do()":
                enabled = True
            elif found == "don't()":
                enabled = False
            elif enabled:
                nums = regex2.match(found).groups()
                answer += int(nums[0])*int(nums[1])
    print("---")
    print(answer)

def main():
    lines = readinput()
    # part1(lines)
    part2(lines)

if __name__=="__main__":
    main()
