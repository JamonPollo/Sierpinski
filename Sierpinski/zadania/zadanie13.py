import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

import random
def is_prime(n, k=5):  # liczba iteracji Miller-Rabin test
    if n < 2: return False
    for p in [2,3,5,7,11,13,17,19,23,29]:
        if n % p == 0: return n == p
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1: continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1: break
        else: return False
    return True

MAX = 4
MAXX = 10
MAXN = 8

licz=0
k=1

while licz<MAX:
    j=4*k+3
    k=k+1
    if is_prime(j):
        print(j)
        licz=licz+1
        for x in range(2, MAXX, 2):
            y = x**x
            for i in range(2, MAXN):  # dla n od 1 do NMAX
                print(f"Dla i = {i}, {x}^(...{i}...)^{x} + 1 mod {j} = {(y + 1) % j}")
                y = y ** x