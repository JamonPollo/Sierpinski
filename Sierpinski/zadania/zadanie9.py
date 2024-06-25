import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

def check_numbers(n):

        sum1 = sum(j**5 for j in range(1, n+1))
        sum2 = sum(j**3 for j in range(1, n+1))
        number = 3 * sum1
        if number % sum2 == 0:
            print(f"Dla n = {n}: 3*(1^5+...+{n}^5) = {number}, 1^3+...+{n}^3 = {sum2}, {number} = {number//sum2} * {sum2}")
        else:
            print(f"Dla n = {n}, wartość wyrażenia nie jest liczbą całkowitą: {number/sum2}")

 # Sprawdza dla pierwszych 10 dodatnich liczb całkowitych n
check_numbers(1000)

#Drukowanie tak jak we wzorze z podstawiona liczba