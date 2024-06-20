import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

def liczby(n):
    an = 2**(2*n+1)-2**(n+1)+1
    bn = 2**(2*n+1)+2**(n+1)+1

    if an % 5 == 0:
        print(f"Dla n = {n}, an = 2^(2n+1) - 2^(n+1) + 1 = {an} = 5*{an//5}.")
    if bn % 5 == 0:
        print(f"Dla n = {n}, bn = 2^(2n+1) + 2^(n+1) + 1 = {bn} = 5*{bn//5}.")

# testujemy funkcję
for i in range(1, 11):  # dla n od 1 do 10
    {liczby(i)}