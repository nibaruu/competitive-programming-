t = int(input())

for _ in range(t):
    a, b, n = map(int, input().split())
    tools = list(map(int, input().split()))

    ans = b
    for x in tools:
        ans += min(x, a - 1)

    print(ans)