test=int(input())
for _ in range(test):
   n,k,x=map(int,input().split())
   min=k*(k+1)//2
   max=k*(2*n-k+1)//2
   if min<=x<=max:
       print("yes")
   else:
       print("no")    