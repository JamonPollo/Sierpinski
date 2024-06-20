import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

def zlozonosc(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return True
    return False

def znajdź_liczby():
    result_2 = []
    result_3 = []
    n = 4
    while len(result_2) < 2 or len(result_3) < 2:
        if zlozonosc(n):
            if (2**n - 2) % n == 0:
                result_2.append(n)
            if (3**n - 3) % n == 0:
                result_3.append(n)
        n += 1
    return result_2, result_3

result_2, result_3 = znajdź_liczby()
print(f"Najmniejsze liczby złożone dla (2^n - 2)/n: {result_2}")
print(f"Najmniejsze liczby złożone dla (3^n - 3)/n: {result_3}")
