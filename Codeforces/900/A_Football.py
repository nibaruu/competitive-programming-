t = input()

f = {'0': 1, '1': 1}

for i in range(1, len(t)):
    if t[i] == t[i-1]:
        f[t[i]] += 1
        if f[t[i]] >= 7:
            print("YES")
            break
    else:
        f[t[i]] = 1
else:
    print("NO")