import sys
n,m = map(int,sys.stdin.readline().rstrip().split(" "))


nameKeyObj ={}
numberKeyObj ={}
for i in range(0,n):
    name = sys.stdin.readline().rstrip()
    nameKeyObj[name] = i+1
    numberKeyObj[str(i+1)] = name

for i in range(0,m):
    input = sys.stdin.readline().rstrip()
    if(input.isdigit()):
        print(numberKeyObj.get(input))
    else:
        print(nameKeyObj.get(input))