import random
from prost import *
from STEPP import *
from hash import *
from math import gcd as bltin_gcd


def coprime2(a, b):
    return bltin_gcd(a, b) == 1


b = int(random.randint(1, 10))
print(b)
p = int(random.randint(1, 10000))
q = int(random.randint(1, 1000))
while (p != (b * q + 1)):
    p = int(random.randint(1, 10000))
    while prost(p) == False:
        p = int(random.randint(1, 10000))
    q = int(random.randint(1, 1000))
    while prost(q) == False:
        q = int(random.randint(1, 1000))
print(p, q)
b = int(random.randint(1, 1000))
g = int(random.randint(1, 1000))
l = ((p - 1) // q)
a = pow(g, l, p)
while a < 1:
    g = int(random.randint(1, 1000))
    a = step((p - 1 // q), p, g)
    print(a)
x = int(random.randint(1, q))
y = step(x, p, a)
m = input()
h = md5(m)
h = int(h, 16) % q
k = int(random.randint(1, q))
r = pow(a, k, p) % q
while r == 0:
    k = int(random.randint(1, q))
    r = step(k, p, a) % q
s = ((k * h) + (x * r)) % q
while s == 0:
    k = int(random.randint(1, q))
    r = step(k, p, a) % q
    while r == 0:
        k = int(random.randint(1, q))
        r = step(k, p, a) % q
    s = ((k * h) + (x * r)) % q
print(m, r, s)
if (r > 0) and (q > r) and (s > 0) and (q > s):
    u1 = ((pow(h, -1, q)) * s) % q
    print(u1)
    u2 = (-r * pow(h, -1, q)) % q
    print(u2)
    u = (pow(a, u1) * pow(y, u2)) % p % q
    print(u, ' = ', r)



