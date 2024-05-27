import sys
n,m = map(int,sys.stdin.readline().rstrip().split(" "))

not_obj = {}

for i in range(0,n):
    name = sys.stdin.readline().rstrip()
    not_obj[name] = 1

for i in range(0,m):
    name = sys.stdin.readline().rstrip()
    if(not_obj.get(name)):
         not_obj[name] = not_obj.get(name)+1
    else:
         not_obj[name] = 1

key_list = [*not_obj]
answer = []
cnt = 0
for key in key_list:
    if(not_obj[key] == 2):
        answer.append(key)
        cnt+=1

answer = sorted(answer)
print(cnt)
for i in answer:
    print(i)
