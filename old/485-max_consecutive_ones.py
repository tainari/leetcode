class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_count = 0
        max_count = 0
        for n in nums:
            if n == 1:
                current_count += 1
            else:
                max_count = max(max_count, current_count)
                current_count = 0
        max_count = max(max_count, current_count)
        return max_count
