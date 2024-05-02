import sys 

while True:
    line = sys.stdin.readline().rstrip()
    if(line == "."): break
    stack = []
    for i in line:
        if(i=='('):
            stack.append(i)
        elif(i==")"):
            if(len(stack) and stack[len(stack)-1]=='('):
                stack.pop()
            else: stack.append(i)
        elif(i=='['):
              stack.append(i)
        elif(i==']'):
            if(len(stack) and stack[len(stack)-1]=='['):
                stack.pop()
            else: stack.append(i)
    print("yes" if len(stack)==0 else "no")