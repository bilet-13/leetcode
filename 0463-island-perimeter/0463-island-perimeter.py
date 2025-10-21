class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = {}

        def dfs(rx, ry):
            edge_count = 0
            stack = [(rx, ry)]
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            visited = [[False for _ in range(len(grid[i]))] for i in range(len(grid))]
            
            while stack:
                x, y = stack.pop()

                if visited[x][y]:
                    continue
                visited[x][y] = True

                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy

                    if nx >= 0 and nx < len(grid) and ny >= 0 and ny < len(grid[i]):
                        if grid[nx][ny] != 1:
                            edge_count += 1

                        elif not visited[nx][ny]:
                            stack.append((nx, ny))
                    else:
                        edge_count += 1

            return edge_count

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i, j)

        return -1