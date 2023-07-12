class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing = 0
        curr = arr.pop(0)
        for i in range(1,1000):
            if i == curr:
                if arr:
                    curr = arr.pop(0)
                else:
                    return curr + (k - missing)
            else:
                missing += 1
            if missing == k:
                return i
        return curr + (k - missing)
