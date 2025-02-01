class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
		#output array
        sums = []
		#keep track of current sum
        curr = 0
		#iterate over numbers, adding each one to curr
		#then appending curr to the output array
        for n in nums:
            curr += n
            sums.append(curr)
        return sums
