import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

def znajdz_x_y(n):
    x = n + 1
    y = x * x  # y = (n + 1) * (n + 1)

    if y**y % x**x == 0:  # Sprawdzamy, czy (y^y) / (x^x) jest liczbą całkowitą
        return x, y
    else:
        return None
VAR = 8
n = VAR   # Wybieramy dowolną dodatnią liczbę całkowitą
result = znajdz_x_y(n)
if result is not None:
    print(f"Dla n = {n}, znalezione x i y to: x = {result[0]}, y = {result[1]}")
else:
    print(f"Dla n = {n} nie znaleziono takich x i y.")