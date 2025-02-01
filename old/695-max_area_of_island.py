class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        def checkIsland(x,y):
			#if not land, or if the land's already been counted, skip
			#makes sure that we don't count the same square multiple times
            if grid[x][y] == 0 or (x,y) in visited:
                return 0
			#otherwise, grid[x][y] is land, so island size at least 1
            land = 1
			#mark as visited
            visited.add((x,y))
			#check all its neighbours and add to size of island
            if 0 < x:
                land += checkIsland(x-1,y)
            if x < rows-1:
                land += checkIsland(x+1,y)
            if 0 < y:
                land += checkIsland(x,y-1)
            if y < cols-1:
                land += checkIsland(x,y+1)
			#return the size of the island
            return land
        
        maxland = 0
        for x in range(rows):
            for y in range(cols):
				#if already seen the island, skip it
                if (x,y) in visited:
                    continue
                land = checkIsland(x,y)
                maxland = max(maxland,land)
        return maxland
                
