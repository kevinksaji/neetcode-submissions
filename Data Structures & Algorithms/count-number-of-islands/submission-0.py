class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = set()
        m, n = len(grid), len(grid[0])
        
        def dfs(i, j):

            if (i, j) in visited or i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == "0":
                return 

            visited.add((i, j))

            for direction in directions:
                newi = direction[0] + i
                newj = direction[1] + j

                dfs(newi, newj)

            
        num_components = 0

        for i in range(m):
            for j in range(n):
                if (i, j) not in visited and grid[i][j] == "1":
                    dfs(i, j)
                    num_components += 1

        return num_components

            

