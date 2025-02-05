"""
https://leetcode.com/problems/ransom-note/description/
Beats 79%
Difficulty: Easy
"""
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note_set = Counter(ransomNote)
        magazine_set = Counter(magazine)
        return all([magazine_set.get(a,0) >= note_set[a] for a in note_set.keys()])