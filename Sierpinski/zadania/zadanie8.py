import math
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

def check_numbers(a,m):

            if a != 1 and m != 0:
                number1 = ((a**m - 1) // (a - 1))
                nwd1 = math.gcd(number1, a - 1)
                nwd2 = math.gcd(a - 1, m)
                if nwd1 != nwd2:
                    print(f"Dla a = {a} i m = {m}, twierdzenie nie jest spełnione.")
                else:
                    print(f"Dla a = {a} i m = {m}, twierdzenie jest spełnione: NWD (({a}^{m} - 1) / ({a} - 1), {a} - 1) = NWD ({a} - 1, {m}) = {nwd1}.")
            else:
                print(f"Dla a = {a} i m = {m}, wyrażenie nie jest zdefiniowane (dzielenie przez zero).")

check_numbers(2,5)  # Sprawdza dla pierwszych 10 dodatnich liczb całkowitych a i m


"""
import math
def check_numbers(n):
    for a in range(2, n+1):
        for m in range(1, n+1):
            number1 = ((a**m - 1) // (a - 1))
            gcd1 = math.gcd(number1, a - 1)
            gcd2 = math.gcd(a - 1, m)
            if gcd1 != gcd2:
                print(f"Dla a = {a} i m = {m}, twierdzenie nie jest spełnione.")
            else:
                print(f"Dla a = {a} i m = {m}, twierdzenie jest spełnione: {gcd1}.")

check_numbers(10)  # Sprawdza dla pierwszych 10 dodatnich liczb całkowitych a i m

#funkcja 2 parametorow pokazuje ze jest rowne ich najmnijeszy wspolny dzielnik,zeby bylo widac wzor z polecenia
"""
