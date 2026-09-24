test=int(input())

for _ in range(test):
    player="Alice"
    a=list(map(int,input()))
    while True:
        f=False
        for i in range(len(a)-1):
            if a[i]!=a[i+1]:
                if player=="Alice":
                    del a[i:i+2]
                    player="Bob"
                    f=True
                    break
                else:
                    del a[i:i+2]
                    player="Alice"
                    f=True
                    break
        if not f:
            break
    if player=="Alice":
                    print("NET")
    else:
                    print("DA")             
    