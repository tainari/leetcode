class Solution:
    def fib(self, n: int) -> int:
        if 0 <= n <= 1:
            return n
        stack = [0,1]
        for i in range(2,n+1):
            val = sum(stack)
            stack.pop(0)
            stack.append(val)
        return stack[-1]
        #RECURSIVE SOLUTION - much slower, less memory
        # if n == 0:
        #     return 0
        # if n <= 2:
        #     return 1
        # return self.fib(n-1) + self.fib(n-2)
