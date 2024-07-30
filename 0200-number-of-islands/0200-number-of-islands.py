class Solution:
    def BFS(self, grid, root):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        vertices = [root]
        queue = [root]

        while queue:
            i, j = queue.pop(0)

            for di, dj in directions:
                ni, nj = i + di, j + dj
                if self.check_one(ni, nj, grid) and (ni, nj) not in vertices:
                    self.add_to_lists((ni, nj), vertices, queue)
        
        return vertices

    def check_one(self, i,j, grid):
        return (grid[i][j] == '1')

    def add_to_lists(self, element, list1, list2):
        list1.append(element)
        list2.append(element)

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        water_surround_grid = []
        found_lands = []

        for i in range(m+2):
            water_surround_grid.append([])
            found_lands.append([])

            for j in range(n+2):
                found_lands[i].append(False)

                if j == 0 or  j == (n+1) or i == 0 or i == (m+1):
                    water_surround_grid[i].append("0")
                else:
                    water_surround_grid[i].append(grid[i-1][j-1])
  
        islands = 0
        for i in range(1, m+1):
            for j in range(1,n+1):
                if water_surround_grid[i][j] == "1" and not found_lands[i][j]:
                    islands += 1

                    adjenct_lands = self.BFS(water_surround_grid,(i, j))
                    for x, y in adjenct_lands:
                        found_lands[x][y] = True
                    

        return islands
