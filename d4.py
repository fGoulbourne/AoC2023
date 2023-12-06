from loader import load
import re


def d1() -> str:
    lines = load()
    out = 0

    for line in lines:
        splt = re.split(r'[|:]', line)

        win = set()
        nums = set()

        wmatch = re.findall(r'\d+', splt[1])
        nmatch = re.findall(r'\d+', splt[2])

        for match in wmatch:
            win.add(match)

        for match in nmatch:
            nums.add(match)

        overlap = win.intersection(nums)

        if len(overlap) != 0:
            out += 2**int(len(overlap) - 1)

    return str(out)


def d2() -> str:
    lines = load()
    counts = dict()

    counter = 0

    for i in range(len(lines)):
        counts[i+1] = 1

    for line in lines:
        counter += 1
        quant = counts[counter]

        splt = re.split(r'[|:]', line)

        win = set()
        nums = set()

        wmatch = re.findall(r'\d+', splt[1])
        nmatch = re.findall(r'\d+', splt[2])

        for match in wmatch:
            win.add(match)

        for match in nmatch:
            nums.add(match)

        overlap = win.intersection(nums)

        for i in range(counter + 1, counter + 1 + len(overlap)):
            counts[i] += quant

    return str(sum(counts.values()))


if __name__ == "__main__":
    print(d1())
    print("")
    print(d2())
