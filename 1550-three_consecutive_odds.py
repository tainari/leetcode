class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
      #submitted the same code three times without changing anything
      #it was faster than 35%, 15%, and 60+% of answers
        cons = 0
        for n in arr:
            if n % 2 == 1:
                cons += 1
                if cons >= 3:
                    return True
            else:
                cons = 0
        return False
