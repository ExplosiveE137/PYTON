import random
import math
from NOD import *
from STEPP import *
from DH_2 import *
from prost import *

def elg():

    m = DH() % 500
    p = int(random.randint(0, 500))
    g = int(random.randint(0, p))
    while (prost(p) == False) or (m >= p) or (prost(g) == False) or (g == p):
        p = int(random.randint(0, 500) + 1)
        g = int(random.randint(0, p))
    ca = int(random.randint(2, p - 2))
    da = step(ca, p, g)
    cb = int(random.randint(2, p - 2))
    db = step(cb, p, g)
    k = int(random.randint(1, p - 1))
    r = step(k, p, g)
    e = m * step(k, p, db) % p
    ms = e * step((p-1-cb), p, r) % p
    print(m, ms)
