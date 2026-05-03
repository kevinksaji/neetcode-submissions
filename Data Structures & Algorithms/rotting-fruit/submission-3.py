class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        # run bfs from every rotten fruit

        directions = [[1, 0], [0, 1],[-1, 0],[0, -1]]

        q = deque()
        time, fresh = 0, 0

        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1

                if grid[r][c] == 2:
                    q.append([r, c])


        while fresh > 0 and q:
            length = len(q)
            for i in range(length):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row in range(len(grid))
                        and col in range(len(grid[0]))
                        and grid[row][col] == 1
                    ):
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1

            time += 1

        return time if fresh == 0 else -1




                    

