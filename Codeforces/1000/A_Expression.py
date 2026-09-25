num=[int(input()) for _ in range(3)]
first=num[0]*num[1]+num[2] 
second=num[0]+num[1]*num[2] 
third=num[0]*(num[1]+num[2]) 
firth=(num[0]+num[1])*num[2]
fifth=num[0]+num[1]+num[2]
sixth=num[0]*num[1]*num[2]

print(max(first,second,third,firth,fifth,sixth))   