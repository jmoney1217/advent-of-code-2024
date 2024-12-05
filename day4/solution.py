import re

regex1 = re.compile("XMAS")
regex2 = re.compile("SAMX")

def readinput():
    # infile = "sample_in.txt"
    # infile = "sample_in2.txt"
    infile = "input.txt"
    with open(infile, 'r') as ifp:
        lines = [ line.strip() for line in ifp.readlines() ]
    return lines        

def part1(lines):
    answer = 0
    data = []
    for li, line in enumerate(lines):
        data.append([])
        for ci, char in enumerate(line):
            data[li].append(char)

    verts = [ [] for _ in range(len(data[0])) ]
    for ri, row in enumerate(data):
        for xi, x in enumerate(row):
            verts[xi].append(x)
    for vert in verts:
        print("vert: {}".format(vert))

    diags = [ [] for _ in range(2*(len(data[0]) + len(data))) ]
    di = 0
    for xi in range(len(data[0])):
        yi = 0
        while xi >= 0 and yi < len(data):
            diags[di].append(data[yi][xi])
            yi+=1
            xi-=1
        print("diags1a: {}".format(diags[di]))
        di+=1
    print("diags1b start")
    for yi in range(1, len(data)):
        xi=len(data[0])-1
        while xi >= 0 and yi < len(data):
            # print("x: {}, y: {}".format(xi, yi))
            diags[di].append(data[yi][xi])
            yi+=1
            xi-=1
        print("diags1b: {}".format(diags[di]))
        di+=1
    
    print("diags2a start")
    for xi in range(len(data[0])):
        yi = 0
        while xi < len(data[0]) and yi < len(data):
            diags[di].append(data[yi][xi])
            yi+=1
            xi+=1
        print("diags2a: {}".format(diags[di]))
        di+=1
    print("diags2b start")
    for yi in range(1, len(data)):
        xi=0
        while xi < len(data[0]) and yi < len(data):
            diags[di].append(data[yi][xi])
            yi+=1
            xi+=1
        print("diags2b: {}".format(diags[di]))
        di+=1

    lines.extend([ ''.join(vert) for vert in verts ])
    lines.extend([ ''.join(diag) for diag in diags ])


    for li, line in enumerate(lines):
        count = len(regex1.findall(line))+len(regex2.findall(line))
        print("{}: {}".format(count, line))
        answer += count

    print("---")
    print(answer)

def part2(lines):
    answer = 0
    data = []
    for li, line in enumerate(lines):
        data.append([])
        for ci, char in enumerate(line):
            data[li].append(char)

    for row in data:
        print(row)

    for yi in range(len(data)):
        for xi in range(len(data[0])):
            try:
                if data[yi][xi] == 'A':
                    str1 = ''.join([data[yi-1][xi-1], data[yi][xi], data[yi+1][xi+1]])
                    str2 = ''.join([data[yi-1][xi+1], data[yi][xi], data[yi+1][xi-1]])
                    if str1 in ["MAS", "SAM"] and str2 in ["MAS", "SAM"]:
                        print("Found X-MAS at [{},{}]".format(yi, xi))
                        answer+=1
            except IndexError:
                pass
    print("---")
    print(answer)

def main():
    lines = readinput()
    part1(lines)
    lines = readinput()
    part2(lines)

if __name__=="__main__":
    main()
