class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [set() for _ in range(9)]
        square = [set() for _ in range(3)]
        for j,row in enumerate(board):
            if j%3 == 0:
                square = [set() for _ in range(3)]
            seen = set()
            for i,n in enumerate(row):
                if n == ".":
                    continue
                if n in seen:
                    return False
                if n in cols[i]:
                    return False
                if n in square[i//3]:
                    return False
                square[i//3].add(n)
                cols[i].add(n)
                seen.add(n)
        return True
