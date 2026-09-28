tests = int(input())

for _ in range(tests):
    a = int(input())
    array = list(input())

    i = 0

    while i < len(array) - 1:
        if array[i] == "(" and array[i+1] == ")":
            del array[i:i+2]
            i = 0
        else:
            i += 1

    print(array.count("("))