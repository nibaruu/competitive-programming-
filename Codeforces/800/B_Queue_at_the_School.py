n, t = map(int, input().split())
array = list(input())

for _ in range(t):
    i = 0
    while i < n - 1:
        if array[i] == "B" and array[i + 1] == "G":
            array[i], array[i + 1] = array[i + 1], array[i]
            i += 2
        else:
            i += 1

print("".join(array))