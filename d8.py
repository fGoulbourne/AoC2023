from loader import load
import re
from math import lcm


def d1() -> str:
    lines = load()

    dirs = lines[0].strip()
    map = dict()

    for line in lines[2:]:
        locs = re.findall(r'[A-Z]+', line)
        map[locs[0]] = (locs[1], locs[2])

    cur = "AAA"
    out = 0
    while cur != "ZZZ":
        cur = map[cur][0] if dirs[out % len(dirs)] == "L" else map[cur][1]
        out += 1

    return str(out)


def d2() -> str:
    lines = load()
    dirs = lines[0].strip()
    map = dict()
    starts = dict()

    for line in lines[2:]:
        locs = re.findall(r'[A-Z0-9]+', line)
        map[locs[0]] = (locs[1], locs[2])

        if locs[0][2] == 'A':
            starts[locs[0]] = 0
    for cur in set(starts.keys()):
        start = cur
        steps = 0

        while cur[2] != 'Z':
            cur = map[cur][0] if dirs[steps % len(dirs)] == "L" else map[cur][1]
            steps += 1

        init = steps

        cur = map[cur][0] if dirs[steps % len(dirs)] == "L" else map[cur][1]
        steps += 1

        while cur[2] != 'Z':
            cur = map[cur][0] if dirs[steps % len(dirs)] == "L" else map[cur][1]
            steps += 1

        starts[start] = (init, steps - init)

    cycles = list(starts.values())
    start = max(x[0] for x in cycles)
    loops = [x[1] for x in cycles]
    offsets = [(start - x[0]) % x[1] for x in cycles]
    step = max(loops)

    out = start

    while max(offsets) != 0:
        offsets = [(x[0] + step) % x[1] for x in zip(offsets, loops)]
        out += step

        sync = []
        for offset in zip(offsets, loops):
            if offset[0] == 0:
                sync.append(offset[1])

        step = lcm(*sync)


    return out





    return str(out)


if __name__ == "__main__":
    print(d1())
    print("")
    print(d2())
