class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        n = len(nums)
        last_small = float("-inf")
        longest = 0

        for i in range(0,n):
            num = nums[i]

            if num-1 == last_small:
                count +=1
                last_small = num
            elif num != last_small:
                count =1
                last_small = num
            longest = max(longest, count)
        return longest

