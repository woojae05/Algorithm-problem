a, b = input().split()
newA = ""
newB = ""
for i in reversed(a):
    newA += i
    a = newA
for i in reversed(b):
    newB += i
    b = newB

if int(a) > int(b):
    print(a)
else:
    print(b)
