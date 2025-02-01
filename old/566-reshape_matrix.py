class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        if rows * cols != r * c:
            return mat
        flat = []
        for row in mat:
            flat.extend(row)
        new = [[0] * c for i in range(r)]
        curr = 0
        for n in range(r):
            for m in range(c):
                new[n][m] = flat[curr]
                curr += 1
        return new
