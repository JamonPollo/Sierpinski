
MAX = 4
for n in range(1,MAX):
    if (n**2 + 1) % (n + 1) == 0:
        print(n)
