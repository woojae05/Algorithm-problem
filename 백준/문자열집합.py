import sys
n,m = map(int,sys.stdin.readline().rstrip().split(" "))

stringObj = {}
for i in range(0,n):
    key = sys.stdin.readline().rstrip()
    stringObj[key] = True


strings = []
for i in range(0,m):
    str = sys.stdin.readline().rstrip()
    strings.append(str)


cnt=0

for str in strings:
    if(stringObj.get(str)):
        cnt+=1

print(cnt)
