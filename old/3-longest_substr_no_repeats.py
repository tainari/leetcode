class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
		#implemented editorial solution: sliding window
		if len(s) <= 1:
            return len(s)
        i = j = 0
        seen = {}
        maxlen = 0
        while j < len(s):
            ch = s[j]
            if ch in seen:
				#move i to be the max of its current value
				#or one to the right of the index of 
				#the last appearance of the character
                i = max(i,seen[ch]+1)
			#check distance between i and j if it beats current max
            maxlen = max(maxlen, j - i + 1)
			#map character's current index in hash
            seen[ch] = j
			#move rightmost index one up
            j += 1
        return maxlen
		## Second attempt, still reads too many times
		# #faster than 16%, less memory than 43%
  #       if len(s) <= 1:
  #           return len(s)
  #       m = 0
  #       for i in range(len(s)):
  #           sub = set()
  #           for ch in s[i:]:
  #               if ch in sub:
  #                   m = max(m,len(sub))
  #                   break
  #               sub.add(ch)
  #           m = max(m,len(sub))
  #       return m
		##inefficient and times out at test case 986/987
        #if s == "":
        #    return 0
        #if len(s) == 1:
        #    return 1
        #l = len(s)
        #subs = {a:None for a in range(1,l+1)}
        #for n,ch in enumerate(s):
        #    for m in range(n+1,l+1):
        #        sub = s[n:m]
        #        if len(sub) == len(set(sub)):
        #            subs[len(sub)]= sub
        #subs = {k:v for k,v in subs.items() if v}
        #m = max(subs.keys())
        #return m

