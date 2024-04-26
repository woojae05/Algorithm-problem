nums = list(map(int,input().split(" ")))

maxLen = max(nums)
index = nums.index(maxLen)
del nums[index]
if(maxLen>=sum(nums)):
    print(nums[0]+nums[1]+sum(nums)-1)
else:
    print(sum(nums,maxLen))