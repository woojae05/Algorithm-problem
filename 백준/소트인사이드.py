n = input()

nums = []
for i in n:
    nums.append(int(i))

nums = reversed(sorted(nums))


print(''.join(map(str,nums)))