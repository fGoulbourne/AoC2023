import re

from loader import load

def p1() -> str:
    lines = load()
    out = 0
    totals = {"red" : 12, "green" : 13, "blue" : 14}

    gid = 0

    for line in lines:
        gid += 1
        valid = True

        matches = re.findall(r'(\d+ (?:(?:red)|(?:green)|(?:blue)))', line)

        for match in matches:
            splt = match.split(" ")

            if int(splt[0]) > totals[splt[1]]:
                valid = False
                break

        if valid:
            out += gid

    return str(out)


def p2() -> str:
    lines = load()
    out = 0

    for line in lines:
        totals = {"red": 0, "green": 0, "blue": 0}
        matches = re.findall(r'(\d+ (?:(?:red)|(?:green)|(?:blue)))', line)

        for match in matches:
            splt = match.split(" ")

            if int(splt[0]) > totals[splt[1]]:
                totals[splt[1]] = int(splt[0])

        out += (totals["red"] * totals["green"] * totals["blue"])

    return str(out)


if __name__ == "__main__":
    print(p1())
    print("")
    print(p2())
