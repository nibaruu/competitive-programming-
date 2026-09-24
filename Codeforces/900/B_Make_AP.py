test=int(input())
for _ in range(test):
    a,b,c=map(int,input().split())
    if (b-a)==(c-b):
        print("YES")
        continue
    else:
        am=(2*b-c)//a
        bm=(a+c)//(2*b)
        cm=(2*b-a)//c
        if am>0 and (2*b-c)%a==0 and (b-a*am)==(c-b):
            print("YES")
            continue
        elif bm>0 and (a+c)%(2*b)==0 and (c-b*bm)==(b*bm-a):
            print("YES")
            continue
        elif cm>0 and (2*b-a)%c==0 and (c*cm-b)==(b-a):
            print("YES")
            continue
        print("NO")


            

        

