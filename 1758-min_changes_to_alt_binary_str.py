class Solution:
    def minOperations(self, s: str) -> int:
		#regardless of length, only two answers: starting with 0 or starting with 0
		#number of changes required to change to string starting with 0 (i.e., if position is even)
        delta = sum([int(int(ch) != n % 2) for n,ch in enumerate(s)])
		#starting with 1 is length(s)-delta, so just take the minimum
        return min(delta, len(s)-delta)
		#############
		#############
		#############
		##initial answer was incorrect because it only accounted for one solution
		##but here's what it was for the sake of posterity
		# s_out = ""
        # ct = 0
        # for n,ch in enumerate(s):
        #     if s_out and ch == s_out[-1]:
        #         s_out += flip[ch]
        #         ct += 1
        #     else:
        #         s_out += ch
        # return ct
