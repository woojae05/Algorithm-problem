s = input()

while True:
    if not(s.count('pi') or s.count('ka') or s.count('chu')):
        break
    s = s.replace('pi', ' ', 1)
    s = s.replace('ka', ' ', 1)
    s = s.replace('chu', ' ', 1)
if len(s.strip()) == 0:
    print('YES')
else:
    print('NO')