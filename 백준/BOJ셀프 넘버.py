originNumbers = set(range(1, 10001))
numbers = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    numbers.add(i)

selfNumbers = sorted(originNumbers-numbers)
print(*selfNumbers, sep="\n")
