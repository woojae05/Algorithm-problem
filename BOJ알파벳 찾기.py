S = input()
List = list('abcdefghijklmnopqrstuvwxyz')
cnt = 0
for i in S:
    for j in range(26):
        if List[j] == i:
            List[j] = str(cnt)
    cnt += 1
for i in range(26):
    if List[i].isalpha():
        List[i] = str(-1)

print(*List)
