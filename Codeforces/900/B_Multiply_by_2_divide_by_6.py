test = int(input())

for _ in range(test):
    move = 0
    a, b = 0, 0
    n = int(input())
    
    while True:
        if n % 2 == 0:
            a += 1
            n = n // 2
        else:
            break

    while True:
        if n % 3 == 0:
            b += 1
            n = n // 3
        else:
            break

    if n==1 and b>=a:
        print(2*b-a)
    else:
        print(-1)    
