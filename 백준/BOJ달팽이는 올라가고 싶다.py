import math
A, B, V = map(int, input().split())
dis = (A-B)
total = (V-B)
print(math.ceil(total/dis))
