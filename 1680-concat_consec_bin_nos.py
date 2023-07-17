#This solution is SO SLOW
#guess i have to learn bitwise operations!

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        def makeBinary(n):
            if n == 1:
                return str(bin(n))[2:]
            return makeBinary(n-1) + str(bin(n))[2:]
        out = makeBinary(n)
        if n < 6:
            return int(out,2)
        return int(out,2) % (10**9 + 7)
