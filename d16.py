from loader import load
import re

lines = load()


class Visit:

    def __init__(self, sym='.'):
        self.sym = sym
        self.hori = False
        self.vert = False


class Beam:
    left = (-1, 0)
    right = (1, 0)
    up = (0, -1)
    down = (0, 1)

    def __init__(self, loc: [int, int], dir: [int, int]):
        self.loc = loc
        self.dir = dir


def addTuple(a: [int, int], b: [int, int]) -> [int, int]:

    x = a[0] + b[0]
    y = a[1] + b[1]

    if x < 0 or x >= len(lines[0]) - 1:
        return None
    if y < 0 or y >= len(lines):
        return None

    return x, y


def d1(start: [int, int]) -> str:
    out = 0

    visits = []

    for line in lines:
        line = line.strip()
        row = []
        for c in line:
            row.append(Visit(c))
        visits.append(row)

    beams = []
    if start[0] == -1:
        beams = [Beam((0, start[1]), Beam.right)]
    elif start[0] >= len(lines[0]) - 1:
        beams = [Beam((len(lines[0]) - 2, start[1]), Beam.left)]
    elif start[1] == -1:
        beams = [Beam((start[0], 0), Beam.down)]
    else:
        beams = [Beam((start[0], len(lines) - 1), Beam.down)]

    while len(beams) != 0:
        next = []

        for beam in beams:
            loc = beam.loc
            dir = beam.dir

            if loc is None:
                continue

            tile = visits[loc[1]][loc[0]]

            match tile.sym:
                case '.':
                    if beam.dir == beam.left or beam.dir == beam.right:
                        if tile.hori:
                            continue
                        tile.hori = True
                    else:
                        if tile.vert:
                            continue
                        tile.vert = True
                    next.append(Beam(addTuple(loc, dir), dir))
                case '/':
                    if beam.dir == beam.left or beam.dir == beam.up:
                        if tile.hori:
                            continue
                        tile.hori = True
                    else:
                        if tile.vert:
                            continue
                        tile.vert = True
                    newDir = (-dir[1], -dir[0])
                    next.append(Beam(addTuple(loc, newDir), newDir))
                case '\\':
                    if beam.dir == beam.left or beam.dir == beam.down:
                        if tile.hori:
                            continue
                        tile.hori = True
                    else:
                        if tile.vert:
                            continue
                        tile.vert = True
                    newDir = (dir[1], dir[0])
                    next.append(Beam(addTuple(loc, newDir), newDir))
                case '-':
                    if tile.hori:
                        continue
                    tile.hori = True

                    next.append(Beam(addTuple(loc, Beam.left), Beam.left))
                    next.append(Beam(addTuple(loc, Beam.right), Beam.right))
                case '|':
                    if tile.vert:
                        continue
                    tile.vert = True

                    next.append(Beam(addTuple(loc, Beam.up), Beam.up))
                    next.append(Beam(addTuple(loc, Beam.down), Beam.down))

        beams = next

    for line in visits:
        for v in line:
            if v.hori or v.vert:
                out += 1

    return str(out)


def d2() -> str:
    out = 0
    mx = len(lines[0]) - 1 #Stupid \n
    my = len(lines)

    for i in range(mx):
        out = max(out, int(d1((i, -1))))
        out = max(out, int(d1((i, my))))

    for i in range(my):
        out = max(out, int(d1((-1, i))))
        out = max(out, int(d1((mx, i))))

    return str(out)


if __name__ == "__main__":
    print(d1((-1, 0)))
    print("")
    print(d2())
