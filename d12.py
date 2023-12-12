from loader import load
import re


def d1() -> str:
    lines = load()
    out = 0

    for line in lines:
        bolts, seqs = line.strip().split(" ")
        out += perms(bolts, seqs, {"0": 1})

    return str(out)


def perms(remain: str, counts: str, dp: dict[str, int]) -> int:
    if len(remain) == 0:
        sum = 0
        if counts in dp.keys():
            sum += dp[counts]
        counts0 = counts + ",0"
        if counts0 in dp.keys():
            sum += dp[counts0]

        return sum

    dpout = dict()

    for k, v in dp.items():

        def dot():
            if int(k.split(",")[-1]) == 0:
                newkey = k
            else:
                newkey = k + ",0"
                if not counts.startswith(newkey[:-2]):
                    return

            if newkey in dpout.keys():
                dpout[newkey] += v
            else:
                dpout[newkey] = v

        def hash():
            trim = re.sub(r'[^,]+$', "", k)
            newkey = trim + str(int(k.split(",")[-1]) + 1)

            if newkey in dpout.keys():
                dpout[newkey] += v
            else:
                dpout[newkey] = v

        match remain[0]:
            case '.':
                dot()
            case '#':
                hash()
            case '?':
                dot()
                hash()

    return perms(remain[1:], counts, dpout)

def d2() -> str:
    lines = load()
    out = 0

    for line in lines:
        bolts, seqs = line.strip().split(" ")
        bolts = ((bolts + '?') * 5)[:-1]
        seqs = ((seqs + ',') * 5)[:-1]
        out += perms(bolts, seqs, {"0": 1})

    return str(out)


if __name__ == "__main__":
    print(d1())
    print("")
    print(d2())
