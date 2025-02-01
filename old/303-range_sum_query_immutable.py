class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sums = [nums[0]]
        for n,i in enumerate(nums[1:]):
            self.sums.append(i + self.sums[n])

    def sumRange(self, left: int, right: int) -> int:
        if left:
            return self.sums[right] - self.sums[left - 1]
        return self.sums[right]
