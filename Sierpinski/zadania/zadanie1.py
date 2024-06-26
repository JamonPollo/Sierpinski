import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

MAX = 6
for n in range(1,MAX):
    if (n**2 + 1) % (n + 1) == 0:
        print(n)