array = []
for i in range(9):
    array.append(int(input()))
for i in range(9):
    if array[i] == max(array):
        print(f'{max(array)}\n{i+1}')
