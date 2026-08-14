def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


arr = [64, 25, 12, 22, 11]

print(selection_sort(arr))



def selection(nums):
    n = len(nums)
    for i in range(0,n):
        min_index = i
        for j in range (i+1,n):
            if nums[j]<nums[min_index]:
                min_index = j
        nums[i],nums[min_index]= nums[min_index],nums[i]
    return nums        
        
                
print(selection([2,35,7,4,3,6,0]))
    