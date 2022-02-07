S = input()
sample = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for j in sample:
    S = S.replace(j, "a")

print(len(S))
