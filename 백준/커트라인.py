N,K = map(int,input().split(" "))

scores = list(map(int,input().split(" ")))

scores = sorted(scores)
print(scores[-K])