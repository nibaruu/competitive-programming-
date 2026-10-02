tests = int(input())

for _ in range(tests):
    s = input()
    
    zeros = s.count("0")
    ones = s.count("1")
    
    need_zero = 0
    need_one = 0
    length = 0

    for i in range(len(s)):
        if s[i] == "0":
            need_one += 1
        else:
            need_zero += 1

        if need_zero > zeros or need_one > ones:
            break

        length += 1

    print(len(s) - length)