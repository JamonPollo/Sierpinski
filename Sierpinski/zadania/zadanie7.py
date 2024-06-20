import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

def check_number():
    number = (20**15 - 1)
    divisor = (11 * 31 * 61)
    if number % divisor == 0:
        print(f"(20^(15) -1) = {number} = 11 * 31 * 61 * {number // divisor}")
    else:
        print(f"(20^(15) -1) / (11 * 31 * 61) nie jest liczbą całkowitą: {number / divisor}")

# Sprawdza, czy (20^15 - 1) jest podzielne przez (11 * 31 * 61)
check_number()


"""
def check_number():
    number = (20**15 - 1) / (11 * 31 * 61)
    if number.is_integer():
        print(f"Wartość wyrażenia jest liczbą całkowitą: {number}")
    else:
        print(f"Wartość wyrażenia nie jest liczbą całkowitą: {number}")

# Sprawdza, czy (20^15 - 1) / (11 * 31 * 61) jest liczbą całkowitą
check_number()
"""