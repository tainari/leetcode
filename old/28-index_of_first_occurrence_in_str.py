class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle:
            return 0
        n = len(needle)
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+n] == needle:
                return i
        return -1
        # try:
        #     return haystack.index(needle)
        # except: 
        #     return -1
