class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #index j at 0 
        j = 0
        #index i at the end
        i = len(numbers)-1
        while j < i:
            n1 = numbers[j]
            n2 = numbers[i]
            delta = target - n1
            #if the needed number is less than what's at ind i, move i index to the left
            if delta < n2:
                i -= 1
            #if the number is correct, huzzah! you win.
            elif delta == n2:
                return [j+1,i+1]
            #otherwise, move index j one to the right
            else:
                j += 1
