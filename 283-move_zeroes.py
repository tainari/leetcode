##Kept rewriting this one until I realized 
#that the speed distribution was basically one point in the histogram
#whoops
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if 0 in set(nums):
            zeroes = 0
            i = 0
            while i < len(nums):
                if nums[i] == 0:
                    nums.pop(i)
                    zeroes += 1
                else:
                    i += 1
            for i in range(zeroes):
                nums.append(0)
        # #attempt 1 beats 49% / 10%
        # if len(nums) > 1 and 0 in set(nums):
        #     i = 0
        #     j = len(nums)
        #     while i <= j:
        #         if nums[i] == 0:
        #             nums.append(nums.pop(i))
        #             j -= 1
        #         else:
        #             i += 1
