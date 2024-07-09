import sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding="utf-8")

def check_number(x):
    for n in range(x+1):
        number=(3**(3*n+3)-26*n-27)
        if number % 169 == 0:
            print(f"Dla n={n}, wartość wyrażenia 3^(3*n+3)-26*n-27 jest liczbą całkowitą: {number} = 169 * {number//169}")

MAX = 13
check_number(MAX)


