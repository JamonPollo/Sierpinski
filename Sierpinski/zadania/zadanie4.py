import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

def check_number(n):

        number = (3**(3*n+3) - 26*n - 27)
        if number % 169 == 0:
            print(f"Dla n = {n}, wartość wyrażenia jest liczbą całkowitą: {number} = 169 * {number // 169}")

check_number(0)