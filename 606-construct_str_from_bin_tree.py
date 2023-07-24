class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        #pattern:
        ##root node = number on its own N
        ##if left child X and right child Y exists, N(X)(Y)
        ##if left child X exists but no Y, N(X)()
        ##vice versa, N()(Y)
        if not root:
            return ""
        left = self.tree2str(root.left)
        right = self.tree2str(root.right)
        if right:
            right = f'({right})'
            if not left:
                left = "()"
            else:
                left = f'({left})'
        elif left:
            left = f'({left})'
        return f'{root.val}{left}{right}'
