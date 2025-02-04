"""
https://leetcode.com/problems/rotate-array/
Beats 72% (runtime)
"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        move_left = nums[-k:]
        for ind in range(len(nums) - k - 1, -1, -1):
            nums[ind + k] = nums[ind]
        for ind in range(len(move_left)):
            nums[ind] = move_left[ind]