import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

def check_number():
    number = (2**70 + 3**70)
    if number % 13 == 0:
        print(f"(2^70 + 3^70) = {number} = 13 * {number // 13}")
    else:
        print(f"(2^70 + 3^70) / 13 nie jest liczbą całkowitą: {number / 13}")

# Sprawdza, czy (2^70 + 3^70) jest podzielne przez 13
check_number()