class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        ROW = len(grid)
        COL = len(grid[0])

        visited = set()
        
        # for every possible island, keep track of the size of potential island

        def dfs(i, j):

            if i < 0 or j < 0 or i >= ROW or j >= COL or (i, j) in visited or grid[i][j] == 0:
                return 0

            visited.add((i, j))
            
            return 1 + dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1)
            

                

        
        retSize = 0
        for i in range(ROW):
            for j in range(COL):
                retSize = max(retSize, dfs(i, j))

        return retSize

        

            

            