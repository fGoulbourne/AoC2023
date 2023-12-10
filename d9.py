from loader import load
import re


def d1() -> str:
    lines = load()
    out = 0

    for line in lines:
        diffs = []
        nums = list(re.findall(r'[^ ]+', line))
        diffs.append([int(n) for n in nums])

        level = 0
        while len(diffs[level]) != 0 and (max(diffs[level]) != 0 or min(diffs[level]) != 0):
            diffs.append([(diffs[level][i+1] - diffs[level][i]) for i in range(len(diffs[level]) - 1)])
            level += 1




        diffs[level].append(0)

        while level != 0:
            level -= 1
            diffs[level].append(diffs[level+1][-1] + diffs[level][-1])

        out += diffs[0][-1]

    return str(out)


def d2() -> str:
    lines = load()
    out = 0

    for line in lines:
        diffs = []
        nums = list(re.findall(r'[^ ]+', line))
        nums.reverse()
        diffs.append([int(n) for n in nums])

        level = 0
        while len(diffs[level]) != 0 and (max(diffs[level]) != 0 or min(diffs[level]) != 0):
            diffs.append([(diffs[level][i + 1] - diffs[level][i]) for i in range(len(diffs[level]) - 1)])
            level += 1

        diffs[level].append(0)

        while level != 0:
            level -= 1
            diffs[level].append(diffs[level + 1][-1] + diffs[level][-1])

        out += diffs[0][-1]

    return str(out)


if __name__ == "__main__":
    print(d1())
    print("")
    print(d2())
