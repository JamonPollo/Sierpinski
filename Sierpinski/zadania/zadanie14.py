import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

def oblicz_wyrazenie(n):

    k=((n+1)**n - 1)
    if k % n**2 == 0:
        print(f"({n}+1)^{n} - 1 = {k} = {k // (n**2)} * ({n}^{2})")
    else:
        print(f"(({n}+1)^{n} - 1) / ({n}^2) = {k / (n**2)}")

# testujemy funkcję
for i in range(1, 11):  # dla n od 1 do 10
    print(f"Dla n = {i}:")
    oblicz_wyrazenie(i)