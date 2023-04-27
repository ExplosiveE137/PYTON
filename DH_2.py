import random
import math
from NOD import *
from STEPP import *


def DH():


    def prost(n):
        i = 2
        for i in range(2, i <= n ** (1 / 2)):
            if n % i == 0:
                return False
        return True


    a = 25
    t = 5
    p = int(random.randint(0, 1000) + 1)
    q = int(2 * p + 1)
    while (prost(q) == False) or (prost(p) == False):
        p = int(random.randint(0, 1000) + 1)
        q = int(2 * p + 1)

    g = int(1 + random.randint(0, (p - 2)))
    while step(g, q, p) == 1:
        g = 1 + random.randint(0, (p - 2))
    XR = random.randint(0, g - 2) + 1
    XD = random.randint(0, g - 2) + 1
    yR = step(XR, p, g)
    yD = step(XD, p, g)
    ZRD = step(XR, p, yD)
    ZDR = step(XD, p, yR)
    return ZDR
