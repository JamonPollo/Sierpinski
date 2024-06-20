import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

MAX = 10
for i in range(1,MAX+1):
    print(f"Dla n = 3^{i} = {3**i} : 2^n + 1 = {2**(3**i)+1} = n * {(2**(3**i) + 1)//(3**i)} ")



def jest_pierwsza(n):
    # Funkcja sprawdza, czy liczba jest pierwsza
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def liczby_pierwsze(mp):
    # Używamy generatora, ponieważ istnieje nieskończenie wiele takich liczb
    m = 0
    p = 0
    while m < mp:
        p = p+1
        if jest_pierwsza(p):
            m += 1
            if (2**p + 1) % p == 0:
                print(f"Dla liczby pierwszej {p}: 2^{p} + 1 = {2**(p)+1} = {p} * {(2**(p) + 1)//(p)}")
MAXP = 10
liczby_pierwsze(MAXP)




