List = []
for i in range(0,9):
        user_input = map(int,input().split(" "))
        tmp_list = list(user_input)
        List.append(tmp_list)
MAX = 0
x = 0
y = 0
for i in range(0,9):
    for j in range(0,9):
          num = List[i][j]
          if(MAX < num):
                MAX = num
                x = i
                y = j

print(MAX)
print(x+1,y+1)