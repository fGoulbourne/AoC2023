from loader import load
import re


def d1() -> str:
    lines = load()
    lines.append('a')

    seeds = []

    maps = [dict() for x in range(7)]


    out = 10**12

    for num in re.findall(r'\d+', lines[0]):
        seeds.append(int(num))

    mapID = -2
    for line in lines:
        if 'a' <= line[0] <= 'z':
            if mapID >= 0 and 0 not in maps[mapID].keys():
                maps[mapID][0] = 0
            mapID += 1
            continue

        if len(line) < 3:
            continue

        splt = line.split(" ")

        dest = int(splt[0])
        src = int(splt[1])
        rng = int(splt[2])

        maps[mapID][src] = dest

        if src + rng not in maps[mapID].keys():
            maps[mapID][src + rng] = src + rng

    for seed in seeds:
        step = seed

        for nextMap in maps:
            ks = list(nextMap.keys())
            ks.sort()
            if step > ks[-1]:
                continue
            val = 0
            i = -1
            while val <= step:
                i += 1
                val = ks[i+1]

            val = ks[i]
            step = nextMap[val] + step - val

        out = min(out, step)

    return str(out)


def d2() -> str:
    lines = load()
    lines.append('a')

    seeds = []

    maps = [dict() for x in range(7)]


    out = 10**12
    matches = re.findall(r'\d+', lines[0])

    for i in range(0, len(matches), 2):
        seeds.append((int(matches[i]), int(matches[i+1]) -1 + int(matches[i])))

    mapID = -2
    for line in lines:
        if 'a' <= line[0] <= 'z':
            if mapID >= 0 and 0 not in maps[mapID].keys():
                maps[mapID][0] = 0
            mapID += 1
            continue

        if len(line) < 3:
            continue

        splt = line.split(" ")

        dest = int(splt[0])
        src = int(splt[1])
        rng = int(splt[2])

        maps[mapID][src] = dest

        if src + rng not in maps[mapID].keys():
            maps[mapID][src + rng] = src + rng

    for seed in seeds:
        out = min(out, seedhelper(seed, 0, maps))

    return str(out)

def seedhelper(seeds: (int, int), j: int, maps: list[dict[int, int]]) -> int:
    lstep = seeds[0]
    hstep = seeds[1]
    nextMap = maps[j]
    ks = list(nextMap.keys())
    ks.sort()
    if lstep >= ks[-1]:
        if j == 6:
            return lstep
        return seedhelper(seeds, j+1, maps)
    val = 0
    i = -1
    while val <= lstep:
        i += 1
        val = ks[i + 1]

    if val <= hstep:
        return min(seedhelper((lstep, val-1), j, maps), seedhelper((val, hstep), j, maps))

    val = ks[i]
    offset = nextMap[val] - val

    if j == 6:
        return lstep + offset

    return seedhelper((lstep + offset, hstep + offset), j+1, maps)



    step = nextMap[val] + step - val


if __name__ == "__main__":
    print(d1())
    print("")
    print(d2())
