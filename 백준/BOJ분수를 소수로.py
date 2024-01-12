import math
n = int(input())

for i in range(n):
    front, back = input().split('.')
    if back.count('('):
        back, cir = back.split('(')
        cir = cir[:-1]
        deno = int(len(cir)*'9'+len(back)*'0')
        mole = int(front+back+cir)-int(front + back)
    else: 
        deno = 10 ** len(back)
        mole = int(front+back)

    gcd = math.gcd(deno,mole)
    print(mole // gcd, deno // gcd, sep='/')

