class Solution:
    def arraySign(self, nums: List[int]) -> int:
        positive = True
        for n in nums:
            if n == 0:
                return 0
            if n < 0:
                positive = not positive
        return 1 if positive else -1
