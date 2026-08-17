nums = [1, 2, 3, 5, 6, 7, 8, 9, 6]

n = len(nums)

nums[:] = [nums[-1]] + nums[0:n-1]

print(nums)



nums = [1, 2, 3, 5, 6, 7, 8, 9, 6]

n = len(nums)
last = nums[n-1]

for i in range(n - 2, -1, -1):
    nums[i+1] = nums[i]

nums[0] = last

print(nums)