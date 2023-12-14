import re
import functools

from loader import load

def p1() -> str:
    lines = load()
    out = []

    for line in lines:
        out.append(int(firstNum(line[::1]) + firstNum(line[::-1])))
    return str(sum(out))

def firstNum(xs):
    if '0' <= xs[0] <= '9':
        return xs[0]
    return firstNum(xs[1:])


def p2() -> str:
    lines = load()
    out = []

    for line in lines:
        out.append(int(secondNum(line)))
    return str(sum(out))

nums = {"one" : "1", "two" : "2", "three" : "3", "four" : "4", "five" : "5", "six" : "6", "seven" : "7", "eight" : "8", "nine" : "9"}
def secondNum(xs: str):
    out = []
    while(len(xs) != 0):
        for n in nums.keys():
            if xs.startswith(n):
                out.append(nums[n])

        if '0' <= xs[0] <= '9':
            out.append(xs[0])
        xs = xs[1:]
    return out[0] + out [-1]




if __name__ == "__main__":
    print(p1())
    print("")
    print(p2())
