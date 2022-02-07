S = input()
cnt = 0

for i in S:
    cnt += 2
    if i <= 'C':
        cnt += 1
    elif i <= 'F':
        cnt += 2
    elif i <= 'I':
        cnt += 3
    elif i <= 'L':
        cnt += 4
    elif i <= 'O':
        cnt += 5
    elif i <= 'S':
        cnt += 6
    elif i <= 'V':
        cnt += 7
    elif i <= 'Z':
        cnt += 8
print(cnt)
