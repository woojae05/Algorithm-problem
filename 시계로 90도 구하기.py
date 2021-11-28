#1분 동안 시침= 0.5 분침=6도
# 1분에  5.5도 발생
# 차이각이 90도 를 찾는다

for i  in range(90,330*12,180):
    h = int(i/330)
    m  = int(i/5.5-60*h)
    print('%002d:%002d'%(h,m))

# print(int(90/330))
# print(count)

# n = int(input()) 
# print(n)

# for i in range(1,n+1):
#     pat+2

# print(pat)
