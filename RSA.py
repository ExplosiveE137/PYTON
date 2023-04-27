import random
from prost import *
from NOD import *
from DH_2 import *


def Kl():
    p = int(random.randint(0, 1000))
    while (prost(p) == False):
        p = int(random.randint(0, 1000))
    q = int(random.randint(0, 1000))
    while (prost(q) == False):
        q = int(random.randint(0, 1000))
    N = p * q
    f = (p - 1) * (q - 1)
    d = int(random.randint(0, f))
    while prost(d) == False:
        d = int(random.randint(0, f))
    c = mass(d, f)
    while ((c * d) % f != 1) or (prost(d) == False):
        d = int(random.randint(0, f))
        c = mass(d, f)
    return c, d, N
