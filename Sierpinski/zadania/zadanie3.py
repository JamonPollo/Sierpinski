import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

MAX = 4
def generator(k):
    n = 1
    licznik = 0
    while licznik < k:
        number = 4*(n**2) + 1
        if number % 5 == 0 and number % 13 == 0:
            print(n,": 4 * ", n, "^2 + 1 =", number, "= 5 *",  number//5, "= 13 *", number//13)
            licznik += 1
        n += 1

# Generuje pierwsze MAX liczb spełniających warunek
generator(MAX)