import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

def sprawdz_liczbe(a):
    return (a ** 10 + 1) % 10 == 0

# testujemy funkcję
for a in range(1, 101):  # dla a od 1 do 100
    if sprawdz_liczbe(a):
        print(a)
