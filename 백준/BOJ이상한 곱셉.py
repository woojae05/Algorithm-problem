a,b = input().split()
result = 0

for i in a :
    for j in b:
        result += int(i)*int(j)

print(result)