import sys
n = int(sys.stdin.readline().rstrip())

stack = []
for i in range(0,n):
    input_num = sys.stdin.readline().rstrip().split(" ")
    num = int(input_num[0])
    if(len(input_num)>1):
        addNum = int(input_num[1])
        stack.append(addNum)
    elif(num==2):
        if(len(stack) != 0):
            print(stack.pop())
        else:print(-1)
    elif(num==3):
        print(len(stack))
    elif(num==4):
       print(1 if len(stack)==0 else 0)
    elif(num==5):
        if(len(stack) != 0):
            lastIndex = len(stack) - 1
            print(stack[lastIndex])
        else:print(-1)
