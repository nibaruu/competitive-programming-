a,b=list(map(int,input().split()))

s=1
i=0

while a>0:
    a-=1
    i+=1

    if i==s*b:
        a+=1
        s+=1

print(i)