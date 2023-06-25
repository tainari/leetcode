class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      #inefficient and times out at test case 986/987
        if s == "":
            return 0
        if len(s) == 1:
            return 1
        l = len(s)
        subs = {a:None for a in range(1,l+1)}
        for n,ch in enumerate(s):
            for m in range(n+1,l+1):
                sub = s[n:m]
                if len(sub) == len(set(sub)):
                    subs[len(sub)]= sub
        subs = {k:v for k,v in subs.items() if v}
        m = max(subs.keys())
        return m
