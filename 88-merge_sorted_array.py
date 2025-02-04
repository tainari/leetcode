"""
https://leetcode.com/problems/merge-sorted-array/
Beats 100%
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            for ind in range(n):
                nums1[ind] = nums2[ind]
            return
        if n == 0:
            return
        ind = len(nums1) - 1
        n -= 1
        m -= 1
        while n >= 0 and m >= 0:
            n1 = nums1[m]
            n2 = nums2[n]
            if n1 > n2:
                nums1[ind] = n1
                ind -= 1
                m -= 1
            elif n2 > n1:
                nums1[ind] = n2
                n -= 1
                ind -= 1
            else:
                nums1[ind] = n1
                ind -= 1
                nums1[ind] = n2
                ind -= 1
                n -= 1
                m -= 1
        while n >= 0 and ind >= 0:
            nums1[ind] = nums2[n]
            ind -= 1
            n -= 1