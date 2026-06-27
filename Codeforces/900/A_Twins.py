n = int(input())
coins = list(map(int, input().split()))

coins.sort(reverse=True)

total = sum(coins)
taken = 0
count = 0

for coin in coins:
    taken += coin
    count += 1

    if taken > total - taken:
        print(count)
        break