class Solution:
    def intToRoman(self, num: int) -> str:
        vals = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        roman_nums = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        out = ""
        while num > 0:
            v = vals.pop(0)
            r = roman_nums.pop(0)
            while num >= v:
                num -= v
                out += r
        return out
