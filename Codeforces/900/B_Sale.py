x,y=list(map(int,input().split()))
list1=list(map(int,input().split()))
sum=0
carry=0
list1.sort()
for i in list1:
    if i <0:
        sum+=abs(i)
        carry+=1
    if carry==y:
        break    
print(sum)        
