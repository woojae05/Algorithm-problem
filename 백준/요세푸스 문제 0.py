import sys
from collections import deque
n,k = map(int,sys.stdin.readline().rstrip().split(" "))

queue = deque()
for i in range(1,n+1):
    queue.append(i)

answer = []
while len(queue):
    cnt = 0
    for i in range(0,k):
        cnt+=1
        if(cnt==k):
            answer.append(queue.popleft())
        else:
            queue.append(queue.popleft())


result = ', '.join(map(str, answer))
print('<{}>'.format(result))
