import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

def oblicz_wyrazenie(n):
    return (2**n + 2) // n

for k in range(1, 11):  # dla n = 2^k, k od 1 do 10
    n = 2**k
    print(f"n = {n}, wartość wyrażenia = {oblicz_wyrazenie(n)}")