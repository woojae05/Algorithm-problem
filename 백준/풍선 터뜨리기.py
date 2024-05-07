import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

nums = list(map(int,sys.stdin.readline().rstrip().split(" ")))

deque1 = deque()

for i in range(0,len(nums)):
    deque1.append([i+1,nums[i]])

answer = []
while len(deque1):
    pos,num = deque1.popleft()
    answer.append(pos)
    if(len(deque1)>1):
        if(num>0):
            for i in range(0,abs(num)-1):
                deque1.append(deque1.popleft())
        else:
            for i in range(0,abs(num)):
                deque1.appendleft(deque1.pop())


result = " ".join(map(str,answer))
print(result)
