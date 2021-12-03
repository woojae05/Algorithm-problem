string =list(input())
str = sorted(set(string))
arr =[]
for i in str:
    arr.append(i)
    arr.append(string.count(i))

for i in range(len(arr)):
    print(arr[i],end="")
