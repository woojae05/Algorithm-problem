import sys 
from collections import deque  

n = int(sys.stdin.readline().rstrip())

ds_type = list(map(int,sys.stdin.readline().rstrip().split(" ")))

initNums = list(map(int,sys.stdin.readline().rstrip().split(" ")))

m = int(sys.stdin.readline().rstrip())

addNums = list(map(int,sys.stdin.readline().rstrip().split(" ")))

deque1 = deque()

numsDeque = deque()

for i in range(0,len(ds_type)):
    if(ds_type[i]==0):
        deque1.append(initNums[i])

for i in addNums:
    numsDeque.append(i)

answer = []
for i in range(0,len(addNums)):
    if(len(deque1)>0):
        answer.append(deque1.pop())
        numsDeque.pop()
    else:answer.append(numsDeque.popleft())


print(*answer)


