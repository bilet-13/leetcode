class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        // for each rotten fruit, start bfs and update the nearest fresh fruit time, 
        // return the max minimum time of that fresh fruit turn to rotten fruit
        int minimumElapse = -1;
        queue<vector<int>> fruits;
        vector<vector<bool>> visited(grid.size(), vector<bool>(grid[0].size(), false));
        vector<pair<int, int>> directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        int numFreshFruits = 0;
        int numVisitedFreshFruits = 0;

        for (auto i = 0; i < grid.size(); ++i) {
            for (auto j = 0; j < grid[0].size(); ++j) {
                if (grid[i][j] == 2) {
                    vector<int> fruit = {i, j, 0};
                    fruits.push(fruit);
                } else if (grid[i][j] == 1) {
                    numFreshFruits++;
                }
            }
        }

        if (numFreshFruits == 0) {
            return 0;
        }

        while (!fruits.empty()) {
            auto size = fruits.size();

            for (auto i = 0; i < size; ++i) {
                auto fruit = fruits.front();
                fruits.pop();

                if (visited[fruit[0]][fruit[1]]) {
                    continue;
                }
                visited[fruit[0]][fruit[1]] = true;

                if (grid[fruit[0]][fruit[1]] == 1) {
                    numVisitedFreshFruits++;
                    minimumElapse = max(minimumElapse, fruit[2]);
                }

                for (const auto& [dx, dy]: directions) {
                    int nx = fruit[0] + dx;
                    int ny = fruit[1] + dy;

                    if (nx >= 0 && nx < grid.size() &&
                        ny >= 0 && ny < grid[0].size() &&
                        !visited[nx][ny] && grid[nx][ny] == 1) {
                            vector<int> neighborFruit = {nx, ny, fruit[2] + 1};
                            fruits.push(neighborFruit);
                        }
                }
            }   
        }
        return numVisitedFreshFruits < numFreshFruits ? -1 : minimumElapse;
    }
};
