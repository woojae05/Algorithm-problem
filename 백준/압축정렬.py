n = int(input())
num_list = list(map(int,input().split(" ")))
set_list = list(set(num_list))
sorted_list = sorted(set_list)
answers = {}

cnt = 0
for i in sorted_list:
    answers[i] = cnt
    cnt+=1

for num in num_list:
    print(answers[num], end=" ")