from gen import *
from xor import *

def Ver():
    print("Введите n")
    n = int(input())
    a = rand_key(n)
    b = rand_key(n)
    c = xor(n, a, b)
    g = xor(n, c, b)
    print(a, g)
