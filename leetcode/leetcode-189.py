def rotate( nums, k) -> None:

    k = k% len(nums)
    nums[:]= nums[-k:] + nums[:-k]
    return nums
    
    
print(rotate([2,3,4,5,6,7],3))

