import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

sys.set_int_max_str_digits(10000)
def check_numbers(n):

        number = (2**(2**(6*n+2)) + 3)
        if number % 19 == 0:
            print(f"Dla k = {n}, (2^(2^(6*{n}+1)) +3) = {number}\n= 19 * {number // 19}")
        else:
            print(f"Dla k = {n}, (2^(2^(6*{n}+1)) +3) nie jest liczbą całkowitą: {number / 19}")

 # Sprawdza dla pierwszych 20 nieujemnych liczb całkowitych k
check_numbers(2)