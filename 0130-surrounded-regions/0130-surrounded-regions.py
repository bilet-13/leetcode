class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
          #         modify those cell to X
        m = len(board)
        n = len(board[0])

        def BFS(r, c):
            # travser the O group
            # mark the visited cell if can not reach board
            queue = deque([(r, c)])
            visited = [[False for _ in range(n)] for _ in range(m)] 
            visited[r][c] = True
            isSurround = True

            while queue:
                x, y = queue.popleft()
                
                if x == 0 or x == m - 1 or y == 0 or y == n - 1:
                   isSurround = False 

                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nx = x + dx
                    ny = y + dy

                    if m > nx >= 0 and n > ny >= 0 and not visited[nx][ny] and board[nx][ny] == 'O':
                        visited[nx][ny] = True
                        queue.append((nx, ny))

            if isSurround:
                for i in range(m):
                    for j in range(n): 
                        if visited[i][j]:
                            board[i][j] = 'X'
                    
            return

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    BFS(i, j)
        return
        