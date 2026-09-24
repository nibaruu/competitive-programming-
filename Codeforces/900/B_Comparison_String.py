test=int(input())

for _ in range(test):

    a=int(input())
    b=list(input())
    current=1
    maximum=1
    for i in range(a-1):

        if b[i]==b[i+1]:
            current+=1
        else:
            current=1

        if current>maximum:
            maximum=current

    print(maximum+1)