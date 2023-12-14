from loader import load
import re


def d1() -> str:
    lines = load()
    out = 0

    for x in range(len(lines[0].strip())):
        i = len(lines)
        for j, line in enumerate(lines):
            line = line.strip()
            match line[x]:

                case 'O':
                    out += i
                    i -= 1
                case '#':
                    i = len(lines) - 1 - j
                case '.':
                    continue

    return str(out)

def transpose(matrix: list[list[chr]]) -> list[list[chr]]:
    return [[matrix[x][y] for x in range(len(matrix))] for y in range(len(matrix[0]))]

def rotate(matrix: list[list[chr]]) -> list[list[chr]]:
    mx = len(matrix[0])
    my = len(matrix)
    out = [["." for x in range(mx)] for y in range(my)]

    for y, line in enumerate(matrix):
        for x, c in enumerate(line):
            out[x][my - y - 1] = matrix[y][x]

    return out

def tilt(matrix: list[list[chr]]) -> list[list[chr]]:
    tiltOut = []
    for x in range(len(matrix[0])):
        i = len(matrix)
        col = ["."] * i
        for j, line in enumerate(matrix):

            match line[x]:

                case 'O':
                    col[i-1] = 'O'
                    i -= 1
                case '#':
                    i = len(matrix) - 1 - j
                    col[i] = '#'
                case '.':
                    continue

        tiltOut.append(col)

    return transpose(tiltOut)[::-1]


def hash(matrix: list[list[chr]]) -> int:
    out = 0
    i = 1
    for line in matrix:
        for c in line:
            if c == 'O':
                out += i
            i *= 2

    return out


def d2() -> str:
    lines = load()
    out = 0



    def cycle(mat: list[list[chr]]):
        n = tilt(mat)
        w = tilt(rotate(n))
        s = tilt(rotate(w))
        e = tilt(rotate(s))
        return rotate(e)

    inlines = []
    for line in lines:
        inlines.append(list(line.strip()))

    hashresults = dict()
    hashresults[0] = hash(inlines)

    invresults = dict()
    invresults[hash(inlines)] = 0


    i = 0
    cur = inlines
    step = -1
    while i < 10**9:
        i += 1
        cur = cycle(cur)
        hsh = hash(cur)

        if hsh in invresults.keys():
            step = i - invresults[hsh]
            break

        hashresults[i] = hsh
        invresults[hsh] = i

    if step == -1:
        return str(hashresults[10**9])

    remain = (10**9 - i) % step

    for i in range(remain):
        cur = cycle(cur)

    i = len(cur)
    for line in cur:

        for c in line:
            if c == 'O':
                out += i

        i -= 1

    return str(out)


if __name__ == "__main__":
    print(d1())
    print("")
    print(d2())
