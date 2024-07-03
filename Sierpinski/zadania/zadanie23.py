import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

def znajdz_n(p, limit):
    result = []
    for n in range(1, limit + 1):  # Przechodzimy przez wszystkie n od 1 do limitu
        if (n * 4 + 1) % p == 0:  # Sprawdzamy, czy n*4 + 1 jest podzielne przez p
            result.append(n)
    return result
VAR = 4
p = VAR  # Wybieramy nieparzystą liczbę pierwszą
MAX = 30
print(znajdz_n(p, MAX))