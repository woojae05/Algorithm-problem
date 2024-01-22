N = int(input())

def giveMoney(money):
    q,d,n,p = 0,0,0,0
    while(True):
        if(money==0):
            break
        if(money>=25):
            money-=25
            q+=1
        elif(money>=10):
            money-=10
            d+=1
        elif(money>=5):
            money-=5
            n+=1
        else:
            money-=1
            p+=1 
    print(q,d,n,p)

for i in range(0,N):
    money = int(input())
    giveMoney(money)

