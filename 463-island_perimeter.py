class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        land = dict()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    land[(r,c)] = 4
        for l in land.keys():
            x,y = l
            land[l] -= int((x-1,y) in land) + int((x+1,y) in land) + int((x,y-1) in land) + int((x,y+1) in land)
        return sum(land.values())
