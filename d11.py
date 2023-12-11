from loader import load
import re


def d1() -> str:
    lines = load()
    out = 0

    matrix = []

    def expand(mat):
        ex = []
        for line in mat:
            hasGal = False
            row = []

            for c in line:
                if c == '\n':
                    continue
                row.append(c)
                if c == '#':
                    hasGal = True

            if not hasGal:
                ex.append(['G' for _ in row])
            ex.append(row)

        return ex

    matrix = expand(lines)
    matrix = transpose(matrix)
    matrix = expand(matrix)
    matrix = transpose(matrix)

    gals = list()

    for i, line in enumerate(matrix):
        for j, c in enumerate(line):
            if c != '#':
                continue

            gals.append((i, j))

    for i, a in enumerate(gals):
        for b in gals[i:]:
            out += abs(a[0] - b[0]) + abs(a[1] - b[1])

    return str(out)


def transpose(matrix: list[list[chr]]) -> list[list[chr]]:
    return [[matrix[x][y] for x in range(len(matrix))] for y in range(len(matrix[0]))]


def d2() -> str:
    lines = load()
    out = 0

    matrix = []

    def expand(mat):
        ex = []
        for line in mat:
            hasGal = False
            row = []

            for c in line:
                if c == '\n':
                    continue
                row.append(c)
                if c == '#':
                    hasGal = True

            if not hasGal:
                ex.append(['G' for _ in row])
            ex.append(row)

        return ex

    matrix = expand(lines)
    matrix = transpose(matrix)
    matrix = expand(matrix)
    matrix = transpose(matrix)

    gals = list()

    for i, line in enumerate(matrix):
        for j, c in enumerate(line):
            if c != '#':
                continue

            gals.append((i, j))
    g = 0
    for i, a in enumerate(gals):
        for b in gals[i:]:

            direct = -1 if a[0] > b[0] else 1

            for j in range(a[0], b[0], direct):
                if matrix[j][a[1]] == 'G':
                    out += 999998

            direct = -1 if a[1] > b[1] else 1

            for j in range(a[1], b[1], direct):
                if matrix[b[0]][j] == 'G':
                    out += 999998

            out += abs(a[0] - b[0]) + abs(a[1] - b[1])
    return str(out)


if __name__ == "__main__":
    print(d1())
    print("")
    print(d2())
