a,b=map(int,input().split() )
array=list(map(int,input().split()))
i=1
while True:
    i=i+array[i-1]
    if i==b:
        print("YES")
        break
    if i>b:
        print("NO")
        break
    