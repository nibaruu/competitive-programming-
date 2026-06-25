number = int(input())

array = list(map(int, input().split()))

if 1 in array:
    print("HARD")
else:
    print("EASY")