import sys
n = int(sys.stdin.readline().rstrip())


enter_obj = {}
for i in range(0,n):
    name, isEnter = sys.stdin.readline().rstrip().split(" ")
    if(isEnter == "enter"):
        enter_obj[name]=True
    else:
        del enter_obj[name]

people =reversed(sorted(list(enter_obj.keys())))
print(*people)