test = int(input())

for _ in range(test):
    n = int(input())

    k = 2

    while (2**k - 1) <= n:
        m = 2**k - 1

        if n % m == 0:
            print(n // m)
            break

        k += 1