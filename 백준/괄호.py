import sys

n = int(sys.stdin.readline().rstrip())

def checkVPS(str):
    stack = []
    isVPS = False
    for char in str:
        if(char == "("):
            stack.append(char)
        else:
            if(len(stack)==0):
                return False
            stack.pop()
    if(len(stack)==0): isVPS=True
    return isVPS


for i in range(0,n):
    input_str = sys.stdin.readline().rstrip()
    print( "YES" if checkVPS(input_str) else "NO")