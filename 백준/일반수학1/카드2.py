from collections import deque
import sys

n = int(sys.stdin.readline().rstrip())

queue = deque()

for i in range(1,n+1):
    queue.append(i)

cnt = 1
while len(queue)!=1:
    if(cnt == 1):
        queue.popleft()
        cnt+=1
    elif(cnt==2):
        queue.append(queue.popleft())
        cnt-=1

print(queue[0])