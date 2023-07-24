# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        self.isBalanced = True
        def maxDepth(root):
            if not root:
                return 0
            if not self.isBalanced:
                return 0
            left = maxDepth(root.left) 
            right = maxDepth(root.right)
            delta = abs(left - right)
            if delta > 1:
                self.isBalanced = False
            return 1 + max(left,right)
        left = maxDepth(root.left)
        right = maxDepth(root.right)
        delta = abs(left - right)
        if delta > 1:
                self.isBalanced = False
        return self.isBalanced
        # max_depth_left = maxDepth(root.left)
        # max_depth_right = maxDepth(root.right)
        # return abs(max_depth_left - max_depth_right) <= 1
