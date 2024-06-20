import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

# Zdefiniujmy maksymalną liczbę wyrazów ciągu do sprawdzenia
max_n = 1000

# Zdefiniujmy listy do przechowywania wyrazów podzielnych przez 5, 13 i 65
div_by_5 = []
div_by_13 = []
div_by_65 = []

# Przejdźmy przez wszystkie wyrazy ciągu do max_n
for n in range(2, max_n + 1):
    term = 2**n - 3  # Obliczamy wyraz ciągu

    # Sprawdzamy, czy wyraz jest podzielny przez 5, 13 lub 65
    if term % 5 == 0:
        div_by_5.append(n)
    if term % 13 == 0:
        div_by_13.append(n)
    if term % 65 == 0:
        div_by_65.append(n)

# Wyświetlamy wyniki
print("Wyrazy podzielne przez 5: ", div_by_5)
print("Wyrazy podzielne przez 13: ", div_by_13)
print("Wyrazy podzielne przez 65: ", div_by_65)
