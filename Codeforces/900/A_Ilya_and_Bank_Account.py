n = input()

if n[0] == '-':
    a = int(n[:-1])
    b = int(n[:-2] + n[-1])
    print(max(a, b))
else:
    print(n)