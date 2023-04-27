import random
from prost import *
from NOD import *
from DH_2 import *
from RSA import *
from STEPP import *

def RRSA():
    A = Kl()
    B = Kl()
    m = int(random.randint(100, 1000))
    while m >= B[2]:
        m = int(random.randint(100, 1000))
    e = step(B[1], B[2], m)
    ms = step(B[0], B[2], e)
    print(m, ms)
