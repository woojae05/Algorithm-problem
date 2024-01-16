List = []
for i in range(0,5):
    user_input = input()
    List.append(list(user_input))

newList = []
for i in range(0,5):
    for j in range(0,len(List[i])):
        if(len(newList)-1 >= j ): newList[j].append(List[i][j])
        else :
            newList.append([List[i][j]])


for i in range(0,len(newList)):
    for j in range(0,len(newList[i])):
        print(newList[i][j],end="")
