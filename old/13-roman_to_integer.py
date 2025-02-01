class Solution:
    def romanToInt(self, s: str) -> int:
        nums = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        s = list(s)
        largest = 0
        total = 0
        while s:
            x = s.pop()
            val = nums[x]
            if val > largest:
                largest = val
            if val < largest:
                val *= -1
            total += val
        return total
