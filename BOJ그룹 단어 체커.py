n = int(input())
cnt = 0
for i in range(n):
    S = input()
    list = []
    for j in range(len(S)):
        for k in S:
            if S[j] != k:
                list.append(k)
print(list)
