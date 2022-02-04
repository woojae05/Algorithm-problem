S = input().upper()
max = 0
sample = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
sMax = ''
for i in sample:
    if max < S.count(i):
        max = S.count(i)
        sMax = i
    elif max == S.count(i) and sMax != i:
        sMax = "?"
print(sMax, end="")
