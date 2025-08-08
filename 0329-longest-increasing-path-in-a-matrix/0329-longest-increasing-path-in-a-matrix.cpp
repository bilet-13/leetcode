class Solution {
public:
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        int n = matrix.size();
        int m = matrix[0].size();

        vector<vector<int>> dp(n, vector<int>(m, 0));
        vector<pair<int, int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

        function<int(int,int)> dfs = [&](int x, int y) {
            if (dp[x][y] != 0) {
                return dp[x][y];
            }

            int maxLength = 1;
            for (auto [dx, dy] : directions) {
                int nx = x + dx;
                int ny = y + dy;

                if (nx >= 0 && nx < n &&
                    ny >= 0 && ny < m && matrix[nx][ny] > matrix[x][y]) {
                        maxLength = max(maxLength, 1 + dfs(nx, ny)); 
                    }
            }
            dp[x][y] = maxLength;
            return dp[x][y];
        };

        int result = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                result = max(result, dfs(i, j));
            }
        }
        return result;
    }
};
