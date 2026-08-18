
def linear_search(nums,terget):
    for i in range(0, len(nums)):
        if nums[i] == terget:
            return True
    
    return -1
       
       
       
nums = [1,2,5,7,4,8,4,9]

terget = 8

print(linear_search(nums,terget))