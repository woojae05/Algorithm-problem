n = int(input())
B = list(map(int, input().split()))
A = list()
for i in range(n):
    A.append(B[i]*(i+1))

for i in range(n):
    for j in range(i):
        A[i] -= A[j]
print(*A)
