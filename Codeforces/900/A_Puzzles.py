a,b=map(int,input().split())
s=list(map(int,input().split()))
s.sort()
res = 1000
for i in range(b - a + 1):
   res= min(res, s[i + a - 1] - s[i])

print(res)