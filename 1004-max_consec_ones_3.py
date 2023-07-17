class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ones = sum(nums)
        zeros = len(nums) - ones
        if k >= zeros:
            return len(nums)
        max_len = 0
        left = right = 0
        num_zeros = 0
        curr_len = 0
        while right < len(nums):
            curr = nums[right]
            curr_len += 1
            if curr == 0:
                num_zeros += 1
                if num_zeros > k:
                    max_len = max(max_len,curr_len-1)
                    while nums[left] != 0:
                        left += 1
                    left += 1
                    num_zeros -= 1
                    curr_len = right - left + 1
            right += 1
        max_len = max(max_len, curr_len)
        return max_len
