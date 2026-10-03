class Solution:
    def jump(self, nums: list[int]) -> int:
        jumps = 0
        cur_end = 0      # end of current jump range
        farthest = 0     # farthest reachable so far

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == cur_end:
                jumps += 1
                cur_end = farthest

        return jumps