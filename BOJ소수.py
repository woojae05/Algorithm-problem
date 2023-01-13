M = int(input())
N = int(input())
List= list()    
def isPrime(n):
    if n==1: False
    else:
        for i in range(2,n):
            if(n%i==0): 
                return False
        return True

for i in range(M,N+1):
    if(isPrime(i)): List.append(i)

if(len(List)>=1):
    print(sum(List))
    print(min(List))
else: print(-1)