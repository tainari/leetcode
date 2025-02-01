#problem: https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
      #obviously 0 has a 0 in it so skip it :) 
      i = 1
      while i < n:
        #if 0 is in the number, move to the next one
        #probably a marginal improvement on speed
        if "0" in str(i):
            i += 1
            continue
        #j is the target minus the value of i 
        j = n-i
        #if j doesn't have a zero in it either, then [i, j] is your answer
        if "0" not in str(j):
            return [i, j]
        #otherwise keep on keepin' on
        i += 1
