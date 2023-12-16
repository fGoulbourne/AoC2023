
def load() -> list[str]:
    lines = open("in.txt")
    out = []
    for line in lines:
        out.append(line.strip())
    return out
