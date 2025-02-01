class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #attempt 2 beats 86%
        return [int(a) for a in list(str(int("".join([str(n) for n in digits]))+1))]
        #attempt 1 beats 4%
        # i = -1
        # firstind = -1 * len(digits) - 1
        # carry = True
        # while carry and i > firstind:
        #     if digits[i] != 9:
        #         carry = False
        #         digits[i] += 1
        #         print(digits)
        #     else:
        #         digits[i] = 0
        #         i -= 1
        #         print(digits)
        # if carry:
        #     digits = [1] + digits
        # return digits
