n = int(input())

answer = 0
for num in range(0,n):
    sum = num
    numStr = str(num)
    for char in numStr:
        sum += int(char)
    if(sum == n):
        answer = num
        break
print(answer)