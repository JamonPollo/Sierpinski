import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

def znajdz_n(limit):
    result = []
    for n in range(1, limit + 1):  # Przechodzimy przez wszystkie n od 1 do limit
        if (n * 2**n + 1) % 3 == 0:  # Sprawdzamy, czy n*2^n + 1 jest podzielne przez 3
            result.append(n)
    return result

MAX = 20
print(znajdz_n(MAX))