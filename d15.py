from loader import load
import re


def d1() -> str:
    lines = load()
    out = 0

    for line in lines:
        line = line.strip()

        parts = line.split(",")

        for part in parts:
            out += hash(part)

    return str(out)


def hash(label: str) -> int:
    out = 0
    for c in label:
        out = ((out + ord(c)) * 17) % 256

    return out

class LinkedList:

    def __init__(self, lbl="", val=0, child=None, parent=None):
        self.lbl = lbl
        self.child = child
        self.parent = parent
        self.val = val

    def removeNode(self, lbl):
        node = self

        while node is not None:

            if node.lbl == lbl:
                node.parent.child = node.child
                if node.child is not None:
                    node.child.parent = node.parent
                return

            node = node.child

    def insert(self, lbl, val):
        node = self

        while True:
            if node.lbl == lbl:
                node.val = val
                return

            if node.child is None:
                node.child = LinkedList(lbl, val, None, node)

            node = node.child

    def totalVal(self):
        out = 0
        node = self
        i = 0
        while node is not None:
            out += node.val * i
            node = node.child
            i += 1

        return out

def d2() -> str:
    lines = load()
    out = 0

    boxes = []

    for _ in range(256):
        boxes.append(LinkedList())

    for line in lines:
        line = line.strip()

        parts = line.split(",")

        for part in parts:
            if '=' in part:
                lbl, val = part.split("=")
                box = boxes[hash(lbl)]
                box.insert(lbl, int(val))

            else:
                lbl = part[:-1]
                box = boxes[hash(lbl)]
                box.removeNode(lbl)

    for i, box in enumerate(boxes):
        out += (i + 1) * box.totalVal()

    return str(out)


if __name__ == "__main__":
    print(d1())
    print("")
    print(d2())
