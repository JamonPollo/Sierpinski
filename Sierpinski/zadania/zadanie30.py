import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

def zlozonosc(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return True
    return False

def znajdz_n(a):
    n = a + 1
    while True:
        if zlozonosc(n) and (a ** n - a) % n == 0:
            return n
        n += 1

a = 2  # Przykładowa wartość a
result = znajdz_n(a)
print(f"Dla a = {a}, liczba złożona n dla której (a^n - a)/n jest liczbą całkowitą wynosi: {result}")
