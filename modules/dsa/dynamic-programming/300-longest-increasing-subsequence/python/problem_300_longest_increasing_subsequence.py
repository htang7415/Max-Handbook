from bisect import bisect_left
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails: list[int] = []
        for value in nums:
            # tails[i] is the smallest possible tail of an increasing subsequence of length i + 1.
            index = bisect_left(tails, value)
            if index == len(tails):
                tails.append(value)
            else:
                tails[index] = value
        return len(tails)
