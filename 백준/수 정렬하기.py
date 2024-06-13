n = int(input())
nums = []
for i in range(0,n):
    num = int(input())
    nums.append(num)

nums = sorted(nums)

for i in nums:
    print(i)