a,b,c,d,e,f = map(int,input().split(" "))


answerX = 0
answerY = 0
for x in range(-999,1000):
    for y in range(-999,1000):
        r1 = (a * x) + (b * y)
        r2 = (d * x) + (e * y)
        if(r1 == c and r2 == f):
            answerX = x
            answerY = y
            break
print(answerX, answerY)