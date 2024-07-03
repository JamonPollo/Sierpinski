import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

MAX = 3
def oblicz_wyrazenie(a, n):
    return (a**n + 1) % n == 0
VAR = 7
a = VAR
m = 0
n = 0
while m < MAX:
    n= n+1
    if oblicz_wyrazenie(a, n):
        m = m+1
        print(f"Dla a = {a}, n = {n}: a^n + 1 = {a**n +1} = {n} * {(a**n + 1) // n}")