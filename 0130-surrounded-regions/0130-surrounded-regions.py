class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
          # not surround region -> the groupd that has 'O' on an edge
        # so change regions that don't have o on an edge
        # dfs for  
        
        def dfs(start_x, start_y):
            stack = [(start_x, start_y)]
            visited = set(stack)

            n = len(board)
            m = len(board[0])
            surrounded = True

            while stack:
                cur_x, cur_y = stack.pop()

                if cur_x == 0 or cur_x == n - 1 or cur_y == 0 or cur_y == m - 1:
                    surrounded = False
                
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx = cur_x + dx
                    ny = cur_y + dy

                    if n > nx >= 0 and m > ny >= 0 and board[nx][ny] == 'O' and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        stack.append((nx, ny))

            if surrounded:
                for x, y in visited:
                    board[x][y] = 'X'

        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    dfs(i, j)

        return
        
        