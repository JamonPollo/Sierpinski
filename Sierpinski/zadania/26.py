def check_sequence(N):
    divisible_by_5 = []
    divisible_by_13 = []
    divisible_by_65 = []

    for n in range(2, N+2):
        sequence_number = 2**n - 3
        if sequence_number % 5 == 0:
            divisible_by_5.append(sequence_number)
        if sequence_number % 13 == 0:
            divisible_by_13.append(sequence_number)
        if sequence_number % 65 == 0:
            divisible_by_65.append(sequence_number)

    return len(divisible_by_5), len(divisible_by_13), len(divisible_by_65)

N = 100  # ilość liczb w ciągu do sprawdzenia
print(check_sequence(N))
