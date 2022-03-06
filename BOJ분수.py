N = int(input())
cnt = 0
while (N > 0):
    cnt += 1
    N -= cnt
if(cnt % 2 == 0):
    print("%d/%d" % (cnt+N, 1-N))
else:
    print("%d/%d" % (1-N, cnt+N))
