class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        new = [[0 for i in range(rows)] for i in range(cols)]
        for row in range(rows):
            for col in range(cols):
                new[col][row] = matrix[row][col]
                pass
        return new
