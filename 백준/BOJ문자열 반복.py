n = int(input())
for i in range(n):
    repeat, S = input().split()
    List = []
    for j in S:
        List.append(j*int(repeat))
    print(*List, sep="")
