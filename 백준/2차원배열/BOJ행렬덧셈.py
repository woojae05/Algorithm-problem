n,m = map(int,input().split(" "))
List = []

for i in range(0,n):
    user_input = map(int,input().split(" "))
    tmpList = list(user_input)
    List.append(tmpList)
for i in range(0,n):
    user_input = map(int,input().split(" "))
    tmpList = list(user_input)
    List.append(tmpList)
for i in range(0,n):
    for j in range(0,m):
        print(List[i][j]+List[i+n][j],end=" ")
    print("")    

