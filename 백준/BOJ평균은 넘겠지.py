n = int(input())
for i in range(n):
    array = list(map(int, input().split()))
    avg = 0
    up = 0
    avg = (sum(array) - array[0])/array[0]
    for j in range(1, array[0]+1):
        if array[j] > avg:
            up += 1
    result = (up/array[0])*100
    print(f'{result:.3f}%')
