##solution with help of official solution

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candiesL = [1] * n
        candiesR = [1] * n
        for ind in range(1,n):
            if ratings[ind] > ratings[ind-1]:
                candiesL[ind] = candiesL[ind-1] + 1
        for ind in reversed(range(0,n-1)):
            if ratings[ind] > ratings[ind+1]:
                candiesR[ind] = candiesR[ind+1] + 1
        finalCandies = [max([a,candiesR[n]]) for n,a in enumerate(candiesL)]
        print(finalCandies)
        return sum(finalCandies)
        
#the original one I came up with: succeeded on 44/48 test cases, but time limit exceeded for one that was 12,000 entries long, alas
#saving for posterity :) 
"""
class Solution:
    def candy(self, ratings: List[int]) -> int:
        #define variables
        n = len(ratings)
        if n == 1:
            return 1
        candies = [1] * n
        middle = int((n - 1)/2)
        change = True
        while change:
            change = False
            for ind in range(0,middle+1):
                #part 1: check the outer leftmost index that hasn't been compared
                indL = ind
                #first, compare to the left index, which might be out of bounds
                indLL = ind - 1
                if indLL >= 0:
                    cLL = candies[indLL]
                    if ratings[indL] > ratings[indLL] and candies[indL] <= cLL:
                        candies[indL] = cLL + 1
                        change = True
                    #elif ratings[indL] < ratings[indLL] and candies[indL] >= cLL:
                    #    candies[indLL] = candies[indL] + 1
                #now, do the right, which will always exist
                indLR = ind + 1
                cLR = candies[indLR]
                if ratings[indL] > ratings[indLR] and candies[indL] <= cLR:
                    candies[indL] = cLR + 1
                    change = True
                #elif ratings[indL] < ratings[indLR] and candies[indL] >= cLR:
                #    candies[indLR] = candies[indL] + 1
                #part 2: check the outer rightmost index that hasn't been compared
                indR = n - 1 - ind
                #first, compare to the right index, which might be out of bounds
                indRR = indR + 1
                if indRR < n:
                    cRR = candies[indRR]
                    if ratings[indR] > ratings[indRR] and candies[indR] <= cRR:
                        candies[indR] = cRR + 1
                        change = True
                    #elif ratings[indR] < ratings[indRR] and candies[indR] >= cRR:
                    #    candies[indRR] = candies[indR] + 1
                #cR = candies[indR]
                indRL = indR - 1
                cRL = candies[indRL]
                if ratings[indR] > ratings[indRL] and candies[indR] <= cRL:
                    candies[indR] = cRL + 1
                    change = True
                #elif ratings[indR] < ratings[indRL] and candies[indR] >= cRL:
                #    candies[indRL] = candies[indR] + 1
        return sum(candies)
"""
