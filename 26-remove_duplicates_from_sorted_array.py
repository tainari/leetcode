"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
Beats 100%
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        for ind in range(len(nums) - 1, -1, -1):
            num = nums[ind]
            if num in seen:
                nums.pop(ind)
            else:
                seen.add(num)
        return len(nums)