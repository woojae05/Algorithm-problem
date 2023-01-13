n = int(input())
List = list(map(int,input().split()))
cnt = 0

def isPrime(n):
    if n==1: False
    else:
        for i in range(2,n):
            if(n%i==0): 
                return False
        return True

for i in List:
    if(isPrime(i)): cnt+=1

print(cnt)