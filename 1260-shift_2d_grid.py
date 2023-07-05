class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        # Can take k % [number of squares] because anything over the initial number
        # will just begin the cycle again
        k = k % (rows*cols)
        # Shift left (not right) in order to 'turn' array the right way 
        shift = k * -1
        # If there's no shift, just return the original grid since nothing moved
        if shift == 0:
            return grid
        # Flatten the array
        flattened = []
        for row in grid:
            flattened.extend(row)
        # Re-stitch the array, taking the items from the end and moving them to
        # the start of the array
        flattened = flattened[shift:] + flattened[:shift]
        # Re-format array into 2D array of correct row/col number and return
        ans = [flattened[n*cols:n*cols+cols] for n in range(len(flattened)//cols)]
        return ans
        ## Attempt 2: This is the most inefficient method. 
        ## After flattening array and re-stitching, iterate over new array
        ## By popping items off of stitched flattened array
        # rows = len(grid)
        # cols = len(grid[0])
        # k = k % (rows*cols)
        # shift = k * -1
        # if shift == 0:
        #     return grid
        # flattened = []
        # for row in grid:
        #     flattened.extend(row)
        # flattened = flattened[shift:] + flattened[:shift]
        # ans = [[0] * cols for _ in range(rows)]
        # for i in range(rows):
        #     for j in range(cols):
        #         ans[i][j] = flattened.pop(0)
        # return ans 
        ## Initial attempt: Iteration over array, calculating
        ## Where new position of number will be and pasting
        ## In new array
        # rows = len(grid)
        # cols = len(grid[0])
        # k = k % (rows*cols)
        # if k == 0:
        #     return grid
        # a = [[0] * cols for row in range(rows)]
        # for i in range(rows):
        #     for j in range(cols):
        #         newcol = (j + k) % cols
        #         newrow = (i + ((j + k) // cols)) % rows
        #         #print("i=",i,"; j=",j,"; k=",k,"; newrow=",newrow,"; newcol=",newcol)
        #         a[newrow][newcol] = grid[i][j]
        #         #print(a)
        # return a
