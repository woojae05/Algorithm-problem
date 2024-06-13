import sys
N = int(sys.stdin.readline().rstrip())


nums = []
for i in range(0,N):
    nums.append(int(sys.stdin.readline().rstrip()))

nums = sorted(nums)

for i in nums:
    print(i)