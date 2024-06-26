import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

MAX = 99
for x in range(-MAX, MAX):
    if x != 3 and (x**3 - 3)%(x-3) == 0:
        print(x)