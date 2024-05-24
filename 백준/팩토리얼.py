n = int(input())
cnt = 1
if(n == 0):cnt = 1
else:
    for i in range(n,1,-1):
        cnt*=i
print(cnt)  