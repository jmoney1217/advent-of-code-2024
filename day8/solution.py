import re, copy
from collections import defaultdict
import itertools

def readinput():
    # infile = "sample_in.txt"
    infile = "input.txt"
    with open(infile, 'r') as ifp:
        lines = [ line.strip() for line in ifp.readlines() ]
    return lines        

def calculate_point_on_line(x1, y1, x2, y2, t):
  x = x1 + t * (x2 - x1)
  y = y1 + t * (y2 - y1)
  return (x, y)

def part1(lines):
    answer = 0
    inputmap = []
    antinodes = []
    antennas = defaultdict(list)

    for li, line in enumerate(lines):
        inputmap.append([])
        antinodes.append([])
        for ci, char in enumerate(line):
            inputmap[li].append(char)
            antinodes[li].append('.')
            if char != '.':
                antennas[char].append((li, ci))

    antinodes2 = copy.deepcopy(antinodes)    
    maxY = len(inputmap)
    maxX = len(inputmap[0])

    for freq, locs in antennas.items():
        if len(locs) < 2:
            continue
        for ptA, ptB in itertools.combinations(locs, 2):
            print("Working on pair: {}: {} x {}".format(freq, ptA, ptB))
            for t in [-1, 2]:
                antinodeX, antinodeY = calculate_point_on_line(ptA[1], ptA[0], ptB[1], ptB[0], t)
                if 0 <= antinodeX < maxX and 0 <= antinodeY < maxY:
                    antinodes[antinodeY][antinodeX] = '#'
            t = 0
            while True:
                antinodeX, antinodeY = calculate_point_on_line(ptA[1], ptA[0], ptB[1], ptB[0], t)
                if 0 <= antinodeX < maxX and 0 <= antinodeY < maxY:
                    antinodes2[antinodeY][antinodeX] = '#'
                else:
                    break
                t += 1
            t = -1
            while True:
                antinodeX, antinodeY = calculate_point_on_line(ptA[1], ptA[0], ptB[1], ptB[0], t)
                if 0 <= antinodeX < maxX and 0 <= antinodeY < maxY:
                    antinodes2[antinodeY][antinodeX] = '#'
                else:
                    break
                t -= 1
                

    answer = sum([ x.count('#') for x in antinodes ])
    
    print("---")
    print(answer)

    answer = sum([ x.count('#') for x in antinodes2 ])

    print("---")
    print(answer)

def main():
    lines = readinput()
    part1(lines)

if __name__=="__main__":
    main()
