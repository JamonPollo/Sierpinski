import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

def znajdz_n(limit):
    result = []
    for n in range(1, limit + 1):  # Przechodzimy przez wszystkie n od 1 do limitu
        if (n * 4 + 1) % 3 == 0:  # Sprawdzamy, czy n*4 + 1 jest podzielne przez 3
            result.append(n)
    return result

limit = 1000  # Ustalamy limit do sprawdzenia
print(znajdz_n(limit))