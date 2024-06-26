import numpy as np
def simplex(c, A, b):
    num_vars = len(c)
    num_constraints = len(A)
    # Dodajemy zmienną sztuczną do każdego równania
    A = np.hstack([A, np.eye(num_constraints)])
    # Tworzymy tablicę Simplex
    table = np.zeros((num_constraints + 1, num_vars + num_constraints + 1))
    table[:-1, :num_vars + num_constraints] = A
    table[:-1, -1] = b
    table[-1, :num_vars] = -c
    # Rozwiązujemy problem
    while np.any(table[-1, :-1] < 0):
        change_column = np.argmin(table[-1, :-1])
        ratios = table[:-1, -1] / table[:-1, change_column]
        change_row = np.where(ratios > 0, ratios, np.inf).argmin()
        change_element = table[change_row, change_column]
        if change_element <= 0:
            raise ValueError("Problem jest nieograniczony")
        # Dzielimy wiersz osi przez element osi
        table[change_row, :] /= change_element
        # Aktualizujemy pozostałe wiersze
        for i in range(num_constraints + 1):
            if i == change_row:
                continue
            table[i, :] -= table[change_row, :] * table[i, change_column]
    # Wyszukujemy wartości zmiennych decyzyjnych
    solution = np.zeros(num_vars)
    for i in range(num_vars):
        col = table[:, i]
        if np.sum(col == 0) == num_constraints and np.sum(col == 1) == 1:
            solution[i] = table[col == 1, -1]
    return table[-1, -1], solution

# Przykład z pdf:
c = np.array([1, 2]) # funkcja celu
A = np.array([[1, 1], [-2, 1]]) # macierz ograniczeń
b = np.array([10, 4]) # wektor ograniczeń
optimal_value, variables = simplex(c, A, b)
print("f(x)=", optimal_value)
print("Wartości zmiennych [x1 , x2]:", variables)
