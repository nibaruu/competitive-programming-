s,n=map(int,input().split())

dragins=[]

for i in range(n):
    a,b=map(int,input().split())
    dragins.append((a-s,b))

dragins.sort()

sum=0

for j,b in dragins:

    if j >= sum:
        print("NO")
        exit()

    sum += b

print("YES")