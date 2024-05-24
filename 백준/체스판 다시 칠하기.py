def getNUm(chessMap):
    cnt1 = 0 
    currentCell = "W"
    for i in range(0,len(chessMap)):
        if(i%2==0):
            currentCell = "B"
        else: currentCell = "W"
        for j in range(0,len(chessMap[i])):
            cell = chessMap[i][j]
            if(cell == currentCell):
                cnt1+=1
                if(cell == "W"):currentCell="B"
                else:currentCell="W"
            else:currentCell = cell


    cnt2 = 0
    for i in range(0,len(chessMap)):
        if(i%2==0):
            currentCell = "W"
        else: currentCell = "B"
        for j in range(0,len(chessMap[i])):
            cell = chessMap[i][j]
            if(cell == currentCell):
                cnt2+=1
                if(cell == "W"):currentCell="B"
                else:currentCell="W"
            else:currentCell = cell
    return min(cnt1,cnt2)

n,m = map(int,input().split(" "))

MAP = []

for i in range(0,n):
    row = input()
    MAP.append(row)

answers = []
for i in range(0,len(MAP)):
    if(len(MAP) - i < 8):continue
    for j in range(0,len(MAP[i])):
        if(len(MAP[i]) - j < 8):continue  
        chessMap= [row[j:j+8] for row in MAP[i:i+8]]
        answers.append(getNUm(chessMap))

print(min(answers))
