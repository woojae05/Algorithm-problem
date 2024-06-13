import sys 
N = int(sys.stdin.readline().rstrip())


nums = {}
cnt = 1
for i in range(0,N):
    num = int(sys.stdin.readline().rstrip())
    if(nums.get(num)== None): 
        nums[num] = 1
    else: 
        nums[num] = nums.get(num)+1



sortedKeys = sorted(nums.keys())

for num in sortedKeys:
    for i in range(0,nums[num]):
        print(num)

