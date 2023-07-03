class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = set(s)
        letters.update(set(t))
        return all([s.count(ch) == t.count(ch) for ch in letters])
