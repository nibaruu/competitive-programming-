x=int(input())
for _ in range(x):
    a=int(input())
    y=a%2020
    b=a//2020
    if y<=b:
        print("YES")
    else:
        print("NO")