from gen import *


def xor(n, a, b):
    c = []
    for i in range(n):
        if a[i] == b[i]:
            c.append(int(0))
        else:
            c.append(int(1))
    return c

