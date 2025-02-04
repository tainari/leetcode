"""
https://leetcode.com/problems/remove-element/description/
Beats 100%
"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        left = 0
        right = len(nums) - 1
        changes = 0
        while left <= right:
            num = nums[left]
            if num == val:
                nums[right], nums[left] = None, nums[right]
                right -= 1
                changes += 1
            else:
                left += 1
        return len(nums) - changes