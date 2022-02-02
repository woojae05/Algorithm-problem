n = int(input())
cnt = 0
for i in range(100, n+1):
    List = []
    for j in str(i):
        List.append(int(j))
    if List[1] - List[0] == List[2]-List[1]:
        cnt += 1
if n < 100:
    print(n)
else:
    print(cnt+99)
