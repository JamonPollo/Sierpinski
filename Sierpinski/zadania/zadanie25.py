import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

import math

def znajdz_n(limit):
    result = []
    for n in range(1, limit + 1, 2):  # Przechodzimy tylko przez nieparzyste n
        if (2 ** math.factorial(n) - 1) % n == 0:  # Sprawdzamy, czy (2^n! - 1) jest podzielne przez n
            result.append(n)
    return result

limit = 5  # Ustalamy limit do sprawdzenia
print(znajdz_n(limit))