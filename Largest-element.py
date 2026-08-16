nums = [3, 6, 8, 4, 8, 3, 7, 8, 4, 7, 6, 8, 5]

largest = nums[0]
n = len(nums)

for i in range(0, n):
    largest = max(largest, nums[i])

print(largest)