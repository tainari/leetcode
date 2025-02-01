# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        nval = root.val
        pval = p.val
        qval = q.val
        if pval < nval and qval < nval:
            return self.lowestCommonAncestor(root.left,p,q)
        if pval > nval and qval > nval:
            return self.lowestCommonAncestor(root.right,p,q)
        return root
