import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

deque1 = deque()
for i in range(0,n):
    input = sys.stdin.readline().rstrip().split(" ")
    num = int(input[0])    
    X = 0
    if(num==1):
        deque1.appendleft(int(input[1]))
    elif(num==2):
        deque1.append(int(input[1]))
    elif(num==3):
        if(len(deque1)==0):
            print(-1)
        else:
            print(deque1.popleft())
    elif(num==4):
        if(len(deque1)==0):
            print(-1)
        else:
            print(deque1.pop())
    elif(num==5):
        print(len(deque1))
    elif(num==6):
        if(len(deque1)==0):
            print(1)
        else:
            print(0)
    elif(num==7):
        if(len(deque1)==0):
            print(-1)
        else:
            print(deque1[0])
    elif(num==8):
        if(len(deque1)==0):
            print(-1)
        else:
            print(deque1[len(deque1)-1])