a, b, c = map(int, input().split())
if(c-b<=0) :
    print(-1)
else : 
    distance=c-b
    result = int(1+(a/distance))
    print(result)
    