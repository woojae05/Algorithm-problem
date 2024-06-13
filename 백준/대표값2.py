import math
nums = []

for i in range(0,5):
    num = int(input())
    nums.append(num)

nums = sorted(nums)
print(sum(nums)//5)
print(nums[2])