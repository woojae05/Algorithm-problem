n = int(input())
snows = list(map(int,input().split(" ")))
if(max(snows)>1440 or sum(snows)>(1440 * 2)):
    print(-1)
else:
    cnt = 0
    while(True):
        if(sum(snows)==0):
            break
        else:
            if(len(snows)>1):
                minIndex = snows.index(min(snows))
                snows[minIndex]-=1
                if(snows[minIndex]==0):
                    del snows[minIndex]
                maxIndex = snows.index(max(snows)) 
                snows[maxIndex]-=1
            else:
                maxIndex = snows.index(max(snows)) 
                snows[maxIndex]-=1
            cnt+=1
    print(cnt)