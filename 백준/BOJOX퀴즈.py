n = int(input())
for i in range(n):
    array = list(input())
    point = 0
    result = 0
    for i in array:
        if i == "X":
            point = 0
        else:
            point += 1
            result += point
    print(result)
