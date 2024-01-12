A = int(input())
B = int(input())
C = int(input())
sum = str(A*B*C)
for i in range(10):
    print(sum.count(str(i)))
