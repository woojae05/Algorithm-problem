N = int(input())
cnt = 1
num = 1
if N == 1:
    print(1)
else:
    while(True):
        num = num + (6 * (cnt))
        if (N <= num):
            break
        cnt += 1
    print(cnt+1)
