import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

def test_liczby(n):
    return (2**n - 1) % n == 0
MAX = 77
# Testujemy funkcję
for n in range(2, MAX):  # dla n od 2 do MAX
    if test_liczby(n):
        print(n) 
        break
else:
    print("Nie znaleziono żadnej liczby")    