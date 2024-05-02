import sys

n = int(sys.stdin.readline().rstrip())
stack1 = list(map(int,sys.stdin.readline().rstrip().split(" ")))[::-1]
stack2 = []

cnt = 1

while len(stack1):
    num = stack1[len(stack1)-1]
    if(cnt==num):
        stack1.pop()
        cnt+=1
    else: 
        length = len(stack2)
        if(length!=0):
            if(stack2[length-1]==cnt):
                cnt+=1
                stack2.pop()
            else:
                stack2.append(stack1.pop())
        else:
            stack2.append(stack1.pop())
    

for i in range(0,len(stack2)):
    if(stack2.pop()==cnt):
        cnt+=1
    else:
        break

print("Nice" if  len(stack2) == 0 else "Sad")
