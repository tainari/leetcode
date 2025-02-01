class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) > 1:
            nums = [(v + nums[n+1]) % 10 for n, v in enumerate(nums[:-1])]
        return nums[0]
