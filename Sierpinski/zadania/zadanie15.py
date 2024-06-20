import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

def oblicz_wyrazenie(n):
    return (2**((2**(n)-1)*n) - 1) // (2**n - 1)

# testujemy funkcję
for i in range(1, 11):  # dla n od 1 do 10
    print(f"n = {i}, wartość wyrażenia = {oblicz_wyrazenie(i)}")
#tak samo jak 14