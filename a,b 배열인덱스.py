n = list(input().split())
print(*sorted(n,key = lambda it: (int(it[1:]),it[0])))