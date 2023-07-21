class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        maxLen = 0
        ct = 0
        for l,w in rectangles:
            sq_side = min(l, w)
            if sq_side == maxLen:
                ct += 1
            elif sq_side > maxLen:
                maxLen = sq_side
                ct = 1
        return ct
