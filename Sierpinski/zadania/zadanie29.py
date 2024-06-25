import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

def NWD(a, b):
    while b:
        a, b = b, a % b
    return a

def znajdz_najmniejsze_n():
    n = 1
    while True:
        if NWD(2 ** n - 2, n) != n and NWD(3 ** n - 3, n) == n:
            return n
        n += 1

smallest_n = znajdz_najmniejsze_n()
print("Najmniejsza liczba n spełniająca warunki: ", smallest_n)