def faktorial(n):
    natija = 1
    i = 2
    while i <= n:
        natija *= i
        i += 1
    return natija

print(faktorial(5))