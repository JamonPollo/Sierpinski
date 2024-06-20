import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

def szukaj_x(n):
    return 2*n - 1
MAX = 7
MAXN = 5

for n in range(1, MAXN):
    x = szukaj_x(n)
    y = x
    print(f"Dla n = {n}, x = {x}")
# testujemy funkcję
    for i in range(1, MAX):  # dla n od 1 do MAX
        print(f"Dla i = {i}, x^(...{i}...)^x + 1 = {y + 1} = {n} * {(y+1)//n}")
        y = y**x

