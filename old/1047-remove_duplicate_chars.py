class Solution:
	def removeDuplicates(self, s: str) -> str:
	    #use stack approach to avoid backtracking 
        s_out = []
        for ch in s:
            if s_out and ch == s_out[-1]:
                s_out.pop()
            else:
                s_out.append(ch)
        return "".join(s_out)
		##First attempt - iterate over string and backtrack if duplicate
		##This solution is faster than only 9% of solutions (but uses less memory than over 80%)
		##Start with index i of 0 and original length l of string
		# i = 0
		# l = len(s)
			##while the string is at least length one and i is 
			##two away from the end of the string, compare chars at indices i and i+1
		# while l > 1 and i < l-1:
			##if they're the same character, delete those two chars
			##step back one step and recalculate length of s
		#     if s[i] == s[i+1]:
		#         s = s[:i] + s[i+2:]
		#         l = len(s)
		#         i = max(0,i-1)
			##otherwise keep on your merry way
		#     else: 
		#         i += 1
			##when you get to the end of the string, return what's left of it 
		# return s
