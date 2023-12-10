from loader import load
import re

dirs = {'|': ((0, -1), (0, 1)),
        '-': ((1, 0), (-1, 0)),
        'F': ((1, 0), (0, 1)),
        'J': ((-1, 0), (0, -1)),
        '7': ((-1, 0), (0, 1)),
        'L': ((1, 0), (0, -1)),
        'S': ((1, 0), (-1, 0), (0, 1), (0, -1)),
        '.': (())
        }

def d1() -> str:
    lines = load()
    maze = []
    out = 0

    cur = (-1, -1)
    for i, line in enumerate(lines):
        if cur != (-1, -1):
            break

        for j, c in enumerate(line):
            if c == 'S':
                cur = (j, i)
                break

    prev = cur
    cur = connected(cur, lines)[0]
    out += 1

    while (lines[cur[1]][cur[0]]) != 'S':
        temp = cur
        cur = [x for x in connected(cur, lines) if x != prev][0]
        prev = temp
        out += 1

    return str(out // 2)


def connected(coords: (int, int), maze: list[str]) -> list[(int, int)]:
    out = list()
    x, y = coords
    pipe = maze[y][x]

    for direct in dirs[pipe]:
        a = x + direct[0]
        b = y + direct[1]

        if 0 <= a <= len(maze[0]) - 1 and 0 <= b <= len(maze) - 1:
            newpipe = maze[b][a]

            if (-direct[0], -direct[1]) in dirs[newpipe]:
                out.append((a, b))

    return out

def d2() -> str:
    lines = load()
    maze = []
    out = 0

    cur = (-1, -1)
    for i, line in enumerate(lines):
        if cur != (-1, -1):
            break

        for j, c in enumerate(line):
            if c == 'S':
                cur = (j, i)
                break

    prev = cur
    vert = {cur}
    hori = set()
    cur = connected(cur, lines)[0]

    while (lines[cur[1]][cur[0]]) != 'S':

        if lines[cur[1]][cur[0]] in {'L', 'J', '7', 'F', '-'}:
            vert.add(cur)
        if lines[cur[1]][cur[0]] == '|':
            hori.add(cur)

        temp = cur
        cur = [x for x in connected(cur, lines) if x != prev][0]
        prev = temp

    for x in range(len(lines[0])):
        vc = 0
        for j in range(len(lines)):
            if (x, j) in vert:
                match lines[j][x]:
                    case '-':
                        vc += 1
                    case 'J':
                        vc += 1
                    case '7':
                        vc += 1

            if (x, j) in vert.union(hori):
                continue

            if vc % 2 == 0:
                continue

            out += 1


    return str(out)


if __name__ == "__main__":
    print(d1())
    print("")
    print(d2())
