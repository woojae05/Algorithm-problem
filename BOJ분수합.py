import math
num1,den1 = map(int,input().split())
num2,den2 = map(int,input().split())
if(den1!=den2):
    num1*=den2
    num2*=den1
    den=den1*den2
result = num1+num2
gc = math.gcd(result,den)
print(int(result/gc),int(den/gc))