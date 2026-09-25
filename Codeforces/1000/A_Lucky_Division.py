num=input()
if num.count('4') + num.count('7') == len(num):
    print("YES")
else:
    lucky=[4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]  
    for i in lucky:
        if int(num) % i == 0:
            print("YES")
            break  
    else:
        print("NO")  