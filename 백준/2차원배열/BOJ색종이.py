Map = []

def paint(x,y):
    cnt = 0
    for i in range(x-1,x+9):
        for j in range(y-1,y +9):
                Map[i][j] = "X"
                cnt+=1

for i in range(0,100):
    row = []
    for j in range(0,100):
        row.append("O")
    Map.append(row)

n = int(input())

List = []
for i in range(0,n):
    x,y = map(int,input().split(" "))
    paint(x,y)

cnt= 0
for i in range(0,len(Map)):
    cnt += Map[i].count("X")
          
          
print(cnt)


# 3 7  4 7
# 3 ~ 13
# 7 ~ 17