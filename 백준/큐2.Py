import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
queue = deque()
for i in range(0,n):
    length = len(queue)
    input = sys.stdin.readline().rstrip().split(" ")
    command = input[0]
    if(command == "push"):
        queue.append(int(input[1]))
    elif(command == "pop"):
        if(length < 1):
            print("-1")
        else:
            print(queue.popleft())
    elif(command == "size"):
        print(length)
    elif(command == "empty"):
        print(1 if length==0 else "0")
    elif(command == "front"):
        print(-1 if length < 1 else queue[0])
    elif(command == "back"):
       print(-1 if length < 1 else queue[length-1])
