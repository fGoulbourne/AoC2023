import re

from loader import load

def p1() -> str:
    lines = load()
    adjacent = False
    num = ""
    out = 0

    for y, line in enumerate(lines):
        for x, c in enumerate(line):

            if '0' <= c <= '9':
                num += c

                for i in range(max(y-1, 0), min(y+2, len(lines))):
                    for j in range(max(x-1, 0), min(x+2, len(line))):
                        s = lines[i][j]
                        adjacent = adjacent or (s != '.' and ('0' > s or '9' < s) and s != "\n")
            else:
                if adjacent:
                    out += int(num)
                adjacent = False
                num = ""
    return str(out)


def p2() -> str:
    lines = load()
    adjacent = False
    fst = (-1, -1)
    num = ""
    out = 0
    outgear = 0
    isgear = False
    update = (-1, -1)
    gear = 0
    gears = dict()

    for y, line in enumerate(lines):
        for x, c in enumerate(line):

            if '0' <= c <= '9':
                if fst == (-1, -1):
                    fst = (x, y)
                num += c

                if update != (-1, -1):
                    gears[update] = (fst, int(num))

                for i in range(max(y-1, 0), min(y+2, len(lines))):
                    for j in range(max(x-1, 0), min(x+2, len(line))):
                        s = lines[i][j]
                        adjacent = adjacent or (s != '.' and ('0' > s or '9' < s) and s != "\n")
                        if s == "*":
                            if (i, j) in gears and gears[(i, j)][0] != fst:
                                isgear = True
                                gear = gears[(i, j)][1]
                            else:
                                gears[(i, j)] = (fst, int(num))
                                update = (i, j)
            else:

                fst = (-1, -1)
                update = (-1, -1)
                if adjacent:
                    out += int(num)

                    if isgear:
                        outgear += gear * int(num)
                        isgear = False
                        gear = 0
                adjacent = False
                num = ""
    return str(outgear)


if __name__ == "__main__":
    print(p1())
    print("")
    print(p2())
