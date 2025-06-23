class Solution {
private:
    void bfs(vector<vector<char>>& board, vector<vector<bool>>& travarsed, int x, int y) {
        int row = board.size();
        int col = board[0].size();
        bool isSurrounded = true;

        queue<pair<int, int>> cells;
        vector<vector<bool>> visited(board.size(), vector<bool>(board[0].size(), false));
        vector<pair<int, int>> directions = {{1, 0}, {-1, 0}, {0, -1}, {0, 1}};

        cells.emplace(x, y);

        while (!cells.empty()) {
            auto [x, y] = cells.front();
            cells.pop();

            if (visited[x][y]) {
                continue;
            }
            visited[x][y] = true;
            travarsed[x][y] = true;

            if (x == 0 || x == row - 1 || y == 0 || y == col - 1) {
                isSurrounded = false;
            }

            for (const auto &[dx, dy]: directions) {
                int nx = x + dx;
                int ny = y + dy;

                if (nx >= 0 && nx < row &&
                    ny >= 0 && ny < col &&
                    !visited[nx][ny] && board[nx][ny] == 'O') {
                        cells.emplace(nx, ny);
                    }
            }
        }

        if (!isSurrounded) {
            return;
        }

        for (int i = 0; i < row; ++i) {
            for (int j = 0; j < col; ++j) {
                if (visited[i][j]) {
                    board[i][j] = 'X';
                }
            }
        }
    }

public:
    void solve(vector<vector<char>>& board) {
        vector<vector<bool>> travarsed(board.size(), vector<bool>(board[0].size(), false));

        for (int i = 0; i < board.size(); ++i) {
            for (int j = 0; j < board[0].size(); ++j) {
                if (board[i][j] == 'O' && !travarsed[i][j]) {
                    bfs(board, travarsed, i, j);
                }
            }
        }
    }
};
