import sys
n = int(sys.stdin.readline().rstrip())

pan = []
for i in range(0,n):
    xy = list(map(int,sys.stdin.readline().rstrip().split(" ")))
    pan.append(xy)


pan = sorted(pan)
for xy in pan:
    print(xy[0],xy[1])