T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())
    floor = N % H
    room = N // H + 1
    if floor == 0:
        room -= 1
        floor = H
    print(floor*100 + room)
