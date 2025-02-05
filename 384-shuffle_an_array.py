"""
https://leetcode.com/problems/shuffle-an-array/description/
beats 98%
Difficulty: Medium
"""
import random
class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums
        self.nums = [x for x in nums]

    def reset(self) -> List[int]:
        return self.original

    def shuffle(self) -> List[int]:
        random.shuffle(self.nums)
        return self.nums
