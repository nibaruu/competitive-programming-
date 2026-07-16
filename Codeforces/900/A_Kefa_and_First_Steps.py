a = int(input())
b = list(map(int, input().split()))

c = 0
k = 0

for i in range(1, a):
    if b[i] >= b[i - 1]:
        c += 1
    else:
        k = max(k, c)
        c = 0

k = max(k, c)

print(k + 1)