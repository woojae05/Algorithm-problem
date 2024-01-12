N = int(input())
firstN = N
cnt = 0
while True:
    cnt += 1
    N1 = N//10
    N2 = (N % 10)
    sum = (N1 + N2) % 10
    N = (N2*10)+sum
    if N == firstN:
        break
print(cnt)
