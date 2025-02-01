class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        #Let an even count = True and an odd count = False.
        #Start with True, since count is 0 for all nums
        #at instantiation
        numdict = {n: True for n in set(nums)}
        for n in nums:
            #flip boolean when you see another instance of n
            numdict[n] = not numdict[n]
        return all(numdict.values())
