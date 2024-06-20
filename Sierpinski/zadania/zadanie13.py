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

MAX = 5
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

"""
for n in range(1, NMAX):
    x = szukaj_x(n)
    y = x
    print(f"Dla n = {n}, x = {x}")
# testujemy funkcję
    for i in range(1, MAX):  # dla n od 1 do MAX
        print(f"Dla i = {i}, x^(...{i}...)^x + 1 = {y + 1} = {n} * {(y+1)//n}")
        y = y**x


"""



"""
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

def sekwencja_podzielna_przez_liczbę():
    max_prime =7 # maksymalna liczba pierwsza do sprawdzenia
    max_x = 10  # maksymalne x do sprawdzenia
    for p in range(5, max_prime):
        if is_prime(p) and p % 4 == 3:
            for x in range(2, max_x, 2):
                y = x
                while y < 1000:  # ograniczenie wyrazów ciągu
                    if pow(y, y, p) == p - 1:  # x^x + 1 ≡ 0 (mod p)
                        print(f"{p} dzieli {x}^{x} + 1")
                        break
                    y = pow(y, y, p)
                else: continue
                break
            else: print(f"Żaden wyraz ciągu nie jest podzielny przez {p} dla dowolnego parzystego x")

sekwencja_podzielna_przez_liczbę()
"""