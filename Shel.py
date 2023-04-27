import random
import math
from NOD import *
from STEPP import *
from DH_2 import *
from prost import *

def Shel():

    cb = int(random.randint(0, 250))
    db = int(random.randint(0, 250))
    ca = int(random.randint(0, 250))
    da = int(random.randint(0, 250))
    p = int(random.randint(0, 500))
    m = DH() % p
    while (prost(p) == False) or (m >= p):
        p = int(random.randint(0, 500) + 1)
    while ((ca*da) % (p-1)) != 1:
        ca = int(random.randint(0, 250))
        da = int(random.randint(0, 250))
    while ((cb*db) % (p-1)) != 1:
        cb = int(random.randint(0, 250))
        db = int(random.randint(0, 250))
    x1 = step(ca, p, m)
    x2 = step(cb, p, x1)
    x3 = step(da, p, x2)
    x4 = step(db, p, x3)
    print(m, x4)

