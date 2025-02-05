"""
https://leetcode.com/problems/insert-delete-getrandom-o1/
Beats 34.3%
Difficulty: Medium
"""
import random
class RandomizedSet:

    def __init__(self):
        self.index_dict = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.index_dict:
            return False
        self.nums.append(val)
        self.index_dict[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.index_dict:
            return False
        ind = self.index_dict[val]
        self.index_dict[self.nums[-1]] = ind
        self.nums[ind], self.nums[-1] = self.nums[-1], self.nums[ind]
        self.nums.pop()
        del self.index_dict[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()