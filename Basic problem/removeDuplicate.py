nums = [2, 4, 7, 4, 2, 7, 4, 9, 11, 35]

unique_nums = []

for num in nums:
    if num not in unique_nums:
        unique_nums.append(num)

print(unique_nums)



nums = [2, 4, 7, 4, 2, 7, 4, 9, 11, 35]

i = 0

while i < len(nums):
    if nums[i] in nums[:i]:
        nums.pop(i)
    else:
        i += 1

print(nums)


print(nums)