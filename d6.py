from loader import load
import re
races = [(61, 430), (67, 1036), (75, 1307), (71, 1150)]
racep2 = (61677571, 430103613071150)
testraces = [(7, 9), (15, 40), (30, 200)]
testracep2 = (71530, 940200)

def d1() -> str:
    out = 1


    for race in races:
        i = 0
        dist = 0
        while dist <= race[1]:
            i += 1
            dist = i * (race[0] - i)

        out *= race[0] - 2 * i + 1

    return str(out)


def d2() -> str:

    i = 0
    dist = 0
    while dist <= racep2[1]:
        i += 1
        dist = i * (racep2[0] - i)
    return str(racep2[0] - 2 * i + 1)






if __name__ == "__main__":
    print(d1())
    print("")
    print(d2())
