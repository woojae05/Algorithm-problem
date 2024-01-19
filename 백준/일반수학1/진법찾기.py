number ="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

N,B = input().split(" ")
B = int(B)
N = "".join(reversed(N))

result = 0
for x in range(len(N)-1,-1,-1):
    result+= number.index(N[x]) * (B**x)
print(result)