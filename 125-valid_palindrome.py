######## IS IT A PALINDROME? #########
##  Tried a few methods for fun :)  ## 
######################################

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([ch.lower() for ch in s if ch.isalnum()])
        r = s[::-1]
        return s == r
        # ## 99% speed / 8% memory
        # s = [ch.lower() for ch in s if ch.isalnum()]
        # for i in range(len(s)//2):
        #     if s[i] != s[-(i+1)]:
        #         return False
        # return True
        # ## 86% speed / 6% memory
        # s = [ch.lower() for ch in s if ch.isalnum()]
        # r = s[::-1]
        # return s == r
