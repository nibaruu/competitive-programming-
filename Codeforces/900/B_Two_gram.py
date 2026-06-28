t=int(input())
string=input()
freq={0: 0}
for i in range(t - 1):
    pair= string[i:i+2]
    if pair in freq:
        freq[pair] += 1
    else:
        freq[pair] = 1
m=max(freq.values())
for key, value in freq.items():
    if value == m:
        print(key)
        break