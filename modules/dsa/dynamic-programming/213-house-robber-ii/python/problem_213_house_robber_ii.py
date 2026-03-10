from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_range(start: int, end: int) -> int:
            prev2 = 0
            prev1 = 0
            for index in range(start, end + 1):
                current = max(prev1, prev2 + nums[index])
                prev2, prev1 = prev1, current
            return prev1

        return max(rob_range(0, len(nums) - 2), rob_range(1, len(nums) - 1))
