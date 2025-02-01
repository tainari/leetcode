class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) == 1:
            return False
        divs = []
        l = len(s)
        for i in range(1,len(s)//2+1):
            if l % i == 0:
                divs.append(i)
        for d in divs:
            sub = s[:d]
            # print(sub, sub*(len(s)//d))
            if sub * (len(s)//d) == s:
                return True
        return False
        #attempt 2 - 31%
        # for i in range(1,len(s)):
        #     sub = s[:i]
        #     if len(s) % len(sub) == 0:
        #         if sub * (len(s)//len(sub)) == s:
        #             return True
        # return False
        ##Attempt 1 - 16%
        # for i in range(1,len(s)):
        #     sub = s[:i]
        #     n = len(s) // len(sub)
        #     if sub * n == s:
        #         return True
        # return False
