import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

MAX = 66
def is_divisible(n):
    # funkcja sprawdzająca czy dana liczba n spełnia podane kryterium
    sum_of_powers = 0
    for i in range(1, n):
        sum_of_powers += i**n
    return sum_of_powers % n == 0

def find_numbers(m):
    # funkcja znajdująca wszystkie liczby całkowite n spełniające podane kryterium
    results = []
    # zakładamy, że szukamy wyników do MAX
    for n in range(2, m):
        if is_divisible(n):
            results.append(n)
    return results

# przykładowe wywołanie funkcji
print(find_numbers(MAX))