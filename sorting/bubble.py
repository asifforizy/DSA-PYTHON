def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


arr = [5, 3, 8, 4, 2]

print(bubble_sort(arr))



def bbs(nums):
    n = len(nums)
    for i in range(n):
        for j in range(0,n-i-1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
    return nums


nums= [5,3,8,4,2]
print(bbs(nums))


def bubble_sort(nums):   
    n = len(nums)
    for i in range(n-2,-1,-1):
        is_sorted = True
        for j in range(0,i+1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
                is_sorted = False
        if is_sorted:
            break
            
    return nums

nums= [5,3,8,4,2,5,7,9,3,5,7]
print(bubble_sort(nums))