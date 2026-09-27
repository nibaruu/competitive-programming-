n,m=map(int,input().split())
a=list(map(int,input().split()))
time=a[0]-1
for i in range(m-1):
    if a[i] <= a[i+1]:
        time += a[i+1] - a[i]  
    else:
        time += n - a[i] + a[i+1]
print(time)