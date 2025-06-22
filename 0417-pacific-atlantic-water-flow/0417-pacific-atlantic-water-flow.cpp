class Solution {
private: 
    void bfs(vector<vector<int>>& heights, queue<pair<int, int>> &cells, vector<vector<bool>> &ocean, int row, int col) {
        vector<vector<bool>> visited(row, vector<bool>(col, false));
        vector<pair<int, int>> directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

        while (!cells.empty()) {
            auto [x, y] = cells.front();
            cells.pop();

            if (visited[x][y]) {
                continue;
            }
            visited[x][y] = true;

            ocean[x][y] = true;

            for (auto &[dx, dy]: directions) {
                int nx = x + dx;
                int ny = y + dy;

                if (nx >= 0 && nx < row &&
                    ny >= 0 && ny < col &&
                    !visited[nx][ny] && heights[nx][ny] >= heights[x][y]) {
                        cells.emplace(nx, ny);
                    }
            }
        }
    }
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        int row = heights.size();
        int col = heights[0].size();

        vector<vector<bool>> toPacific(row, vector<bool>(col, false));
        vector<vector<bool>> toAtlantic(row, vector<bool>(col, false));
        queue<pair<int, int>> cells;
        vector<vector<int>> result;

        for (int i = 0; i < row; ++i) {
            cells.emplace(i, 0);
        }
        for (int j = 0; j < col; ++j) {
            cells.emplace(0, j);
        }
        bfs(heights, cells, toPacific, row, col);

        for (int i = 0; i < row; ++i) {
            cells.emplace(i, col - 1);
        }
        for (int j = 0; j < col; ++j) {
            cells.emplace(row - 1, j);
        }
        bfs(heights, cells, toAtlantic, row, col);
        
        for (int i = 0; i < row; ++i) {
            for (int j = 0; j < col; ++j) {
                if (toAtlantic[i][j] && toPacific[i][j]) {
                    vector<int> cell = {i, j};
                    result.push_back(cell);
                }
            }         
        }

        return result;
    }
};
