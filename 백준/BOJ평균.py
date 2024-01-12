n = int(input())
avg = 0
scores = list(map(int, input().split()))
max = max(scores)
for i in range(n):
    scores[i] = scores[i]/max*100
    avg += scores[i]
print(avg/n)
