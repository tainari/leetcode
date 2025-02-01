class Solution:
    def minimumMoves(self, s: str) -> int:
        if set(s) == {"O",}:
            return 0
        ind = 0
        conversions = 0
		#because you can't turn 0->X, just need to find all places where X exists
		#skip 3 when you find an X
        while ind < len(s):
            if s[ind] == "X":
                conversions += 1
                ind += 2
            ind += 1
        return conversions
