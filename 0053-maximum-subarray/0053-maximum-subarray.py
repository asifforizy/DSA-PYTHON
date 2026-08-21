class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0 
        maxi = float("-inf")
        n=len(nums)
        total = 0
        for i in range(0,n):
            total=total+nums[i]
            maxi = max(maxi,total)
            if total<0:
                total = 0
        return maxi
