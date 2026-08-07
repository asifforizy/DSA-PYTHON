def frequencyMap(nums):
    freq = dict()
    for i in  range(0, len(nums)):
        if nums[i] in freq:
            freq[nums[i]] += 1
        else:
            freq[nums[i]] = 1
    
    return freq


nums = [3,34,5,23,44,3,4,54,3,4, 5,5,3,7,6,8,8]
print(frequencyMap(nums))

#  ! better solution 

def betterfrequencyMap(nums):
    freq = dict()
    n = len(nums)
    for i in  range(0, n):
        freq[nums[i]] = freq.get(nums[i],0)+1
    
    
    return freq


nums = [3,34,5,23,44,5,3,7,6,8,8]
print(betterfrequencyMap(nums))

 