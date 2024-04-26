n = int(input())

def isPrime(num):
    if(num==1):
        return False
    for i in range(2,int(num/2)+1):
        if(num%i==0):
            return False
    return True

def getGoldNum(num):
    for i in range(int(num/2),1,-1):
        num2 = num-i
        if(isPrime(i) and isPrime(num2)):
            return [i,num2]


for i in range(0,n):
    num = int(input())
    answer = getGoldNum(num)
    print(answer[0],answer[1])    
