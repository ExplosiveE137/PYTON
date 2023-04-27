import random
from prost import *
from STEPP import *
from hash import *
from math import gcd as bltin_gcd


def coprime2(a, b):
    return bltin_gcd(a, b) == 1

p = int(random.randint(0, 1000))
while prost(p) == False:
    p = int(random.randint(0, 1000))
q = int(random.randint(0, p))
while prost(q) == False:
    q = int(random.randint(0, p))
N = p * q
f = (p - 1) * (q - 1)
d = int(random.randint(1, p-1))
while coprime2(d, f) == False:
    d = int(random.randint(1, p - 1))
c = pow(d, -1, f)
print(N, d)
m = input()
y = md5(m)
y = int(y, 16) % p
s = step(c, N, y)
print(m, s)
w = step(d, N, s)
print(w, ' = ', y)
