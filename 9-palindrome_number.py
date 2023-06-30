class Solution:
    def isPalindrome(self, x: int) -> bool:
        xs  = list(str(x))
        return xs == xs[::-1]
