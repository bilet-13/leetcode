class Solution {
private:

public:
    int swimInWater(vector<vector<int>>& grid) {
        // find minimum maximum edge
        // minimum spanning tree?
        int n = grid.size();
        int resultTime = -1;
        vector<vector<bool>> visited(n, vector<bool>(n, false));
        vector<pair<int, int>> directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<tuple<int, int, int>>> pq;
        
        pq.emplace(grid[0][0], 0, 0);

        while (!pq.empty()) {
            auto [time, x, y] = pq.top();
            pq.pop();

            if (visited[x][y]) {
                continue;
            }
            visited[x][y] = true;

            resultTime = max(time, resultTime);
            if (x == n - 1 && y == n - 1) {
                return resultTime;
            }

            for (const auto& [dx, dy] : directions) {
                int nx = x + dx;
                int ny = y + dy;

                if (nx >= 0 && nx < n && 
                    ny >= 0 && ny < n && 
                    !visited[nx][ny]) {
                    pq.emplace(grid[nx][ny], nx, ny);
                }
            }
        }
        return resultTime;
    }
};
