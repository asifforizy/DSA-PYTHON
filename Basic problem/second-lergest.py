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


def second_largest(nums):
    l = float('-inf')
    sl = float('-inf')
    n = len(nums)

    for i in range(n):
        l = max(l, nums[i])

    for i in range(n):
        if nums[i] > sl and nums[i] != l:
            sl = nums[i]

    return sl


nums = [2, 4, 7, 4, 2, 7, 4, 9, 11, 35]

print(second_largest(nums))


#! optimal solution

def second_largest(nums):
    largest = float('-inf')
    second = float('-inf')

    for num in nums:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num

    return second

nums = [2, 4, 7, 4, 2, 7, 4, 9, 11, 35]
print(second_largest(nums))





