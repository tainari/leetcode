class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n_rows = len(matrix)
        n_cols = len(matrix[0])
        nonzero_cols = list(range(n_cols))
        mod_rows = set()
        mod_cols = set()
        for r in range(n_rows):
            for c in range(n_cols):
                if matrix[r][c] == 0:
                    mod_rows.add(r)
                    mod_cols.add(c)
        for r in list(mod_rows):
            matrix[r] = [0]*n_cols
        for c in list(mod_cols):
            for r in range(n_rows):
                matrix[r][c] = 0
        
