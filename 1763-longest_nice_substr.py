class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) <= 1:
            return ""
        maxlen = 0
        maxstr = ""
        for left in range(0,len(s)-1):
            for right in range(max(2,maxlen),len(s)+1):
                substr = s[left:right]
                set_substr = list(set(substr))
                nice = all([x.lower() in substr and x.upper() in substr for x in set_substr])
                if nice and len(substr) > maxlen:
                    maxlen = len(substr)
                    maxstr = substr
        return maxstr
