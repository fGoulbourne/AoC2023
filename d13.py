from loader import load
import re


def d1() -> str:
    lines = load()

    areas = []
    area = []
    for line in lines:
        line = line.strip()
        if len(line) > 1:
            area.append(line)
        else:
            areas.append(list(area))
            area = []
    areas.append(list(area))

    out = 0

    for temp, area in enumerate(areas):

        cur = 1
        mx = 0
        i = 0
        while i < len(area):
            line = area[i]

            if area[cur] != line:
                mx += 1
                cur = mx
                i = mx + 1

            else:
                cur -= 1
                i += 1
                if cur == -1:
                    out += 100 * (mx + 1)
                    mx = i
                    cur = i
                    break

        if mx != cur:
            out += 100 * (mx + 1)

        mx = 0
        cur = 1
        i = 0
        tarea = transpose(area)
        while i < len(tarea):
            line = tarea[i]

            if tarea[cur] != line:
                mx += 1
                cur = mx
                i = mx + 1

            else:
                cur -= 1
                i += 1
                if cur == -1:
                    out += mx + 1
                    mx = i
                    cur = i
                    break

        if mx != cur:
            out += mx + 1

    return str(out)

def transpose(matrix: list[str]) -> list[str]:
    return [''.join([matrix[x][y] for x in range(len(matrix))]) for y in range(len(matrix[0]))]

def d2() -> str:
    lines = load()

    areas = []
    area = []
    for line in lines:
        line = line.strip()
        if len(line) > 1:
            area.append(line)
        else:
            areas.append(list(area))
            area = []
    areas.append(list(area))

    out = 0


    for temp, area in enumerate(areas):
        diffs = 0
        found = False
        cur = -2
        mx = -1
        i = 0
        while i < len(area):

            for x, y in zip(area[i], area[cur]):
                if x != y:
                    diffs += 1

            if diffs > 1 or cur == -2:
                diffs = 0
                mx += 1
                cur = mx
                i = mx + 1

            else:
                cur -= 1
                i += 1
                if i == len(area) and diffs == 0:
                    cur = 1
                    diffs = 2
                    i = 1
                if cur == -1 and diffs == 1:
                    out += 100 * (mx + 1)
                    found = True
                    mx = i
                    cur = i
                    break

        if mx != cur:
            out += 100 * (mx + 1)
            found = True
            continue

        if found:
            continue

        mx = -1
        cur = -2
        i = 0

        tarea = transpose(area)

        while i < len(tarea):

            for x, y in zip(tarea[i], tarea[cur]):
                if x != y:
                    diffs += 1

            if diffs > 1 or cur == -2:
                diffs = 0
                mx += 1
                cur = mx
                i = mx + 1

            else:
                cur -= 1
                i += 1
                if i == len(tarea) and diffs == 0:
                    cur = 1
                    diffs = 2
                    i = 1
                if cur == -1 and diffs == 1:
                    out += mx + 1
                    mx = i
                    cur = i
                    break

        if mx != cur:
            out += mx + 1

    return str(out)


if __name__ == "__main__":
    print(d1())
    print("")
    print(d2())
