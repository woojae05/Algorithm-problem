n,m =map(int,input().split())

for i in range(n,m+1):
    isprime=True
    if i<=1:
        continue
    for j in range(2,int(i**0.5)+1):
        if not i%j:
            isprime=False
            break
    if isprime:
        print(i)