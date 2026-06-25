t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input()

    freq = {}

    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    odd = 0

    for cnt in freq.values():
        if cnt % 2 == 1:
            odd += 1

    if odd <= k + 1:
        print("YES")
    else:
        print("NO")