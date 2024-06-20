import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

def test_liczby(n):
    return (2**n - 1) % n == 0

# Testujemy funkcję
for n in range(2, 1000):  # dla n od 2 do 100
    if test_liczby(n):
        print(n)
