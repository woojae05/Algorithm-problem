a1,a0 = map(int,input().split(" "))
c = int(input())
n = int(input())

f1 = (a1 * n) + a0
g1 = c * n

if(f1 <= g1):print(1)
else:print(0)