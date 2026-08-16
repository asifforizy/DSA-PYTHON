nums = [3, 6, 8, 4, 8, 3, 7, 8, 4, 7, 6, 8, 5]

largest = nums[0]
second_largest = float('-inf')

for i in range(1, len(nums)):
    if nums[i] > largest:
        second_largest = largest
        largest = nums[i]
    elif nums[i] > second_largest and nums[i] != largest:
        second_largest = nums[i]

print("Largest:", largest)
print("Second largest:", second_largest)