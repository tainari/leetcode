class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        n = (num + 3)/3
        if n == int(n):
            return list(range(int(n)-2,int(n)+1))
        return []
#would have been better to use modulo
#since n + (n+1) + (n+2) = 3n+3 which must be divisible by three
#so better answer: 
#return [] if num % 3 else [n//3, n//3+1, n//3+2]
