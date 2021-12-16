n, k = map(int,input().split())
cnt = 0
while(1):
    if(n==1):
        break
    else:
        if(n>=k):
            if(n%k==0):
                n=n/k
            elif(n%k!=0):
                n-=1
        else:
            n-=1
    cnt+=1

print(cnt+1)