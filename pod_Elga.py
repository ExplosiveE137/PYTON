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
g = int(random.randint(0, p))
while prost(g) == False:
    g = int(random.randint(0, p))
x = int(random.randint(1, p-1))
y = step(x, p, g)
m = input()
h = md5(m)
h = int(h, 16) % (p - 1)
print(h)
k = int(random.randint(1, p-1))
while coprime2(k, (p - 1)) == False:
    k = int(random.randint(1, p - 1))
r = step(k, p, g)
print(r)
l = (h - (x * r)) % (p - 1)
s = (pow(k, -1, (p - 1)) * l) % (p - 1)
pod = [m, r, s]
print(pod, ' Подпись')
pr1 = (pow(y, r) * pow(r, s)) % p
pr2 = step(h, p, g)
print(pr1, ' = ', pr2)
