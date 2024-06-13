import sys
n = int(sys.stdin.readline().rstrip())

pan = []
for i in range(0,n):
    xy = list(map(int,sys.stdin.readline().rstrip().split(" ")))
    xy.reverse()
    pan.append(xy)


pan.sort()
for xy in pan:
    print(xy[1],xy[0])