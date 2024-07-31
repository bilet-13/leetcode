class Solution:
    def BFS(self, board, root):
        cells = [root]
        queue = [root]

        while queue:
            x, y = queue.pop(0)
            #board[x][y] = 'X'
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            
            for dx, dy in directions:
                nx, ny = x+dx, y +dy
                
                if 0<=nx<len(board) and 0<=ny<(len(board[0])) and board[nx][ny] == 'O':
                    cells.append((nx, ny))
                    board[nx][ny] = 'X'
                    queue.append((nx, ny))
        
        
        return cells

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        not_surround_cells = []

        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i == 0 or i == (len(board) - 1) or j == 0 or j ==(len(board[0]) - 1) ) and board[i][j] == 'O':
                    not_surround_cells += self.BFS(board, (i, j))

        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = 'X'
        
        for x, y in not_surround_cells:
            board[x][y] = 'O'
