class Solution {
private: 
    int bfs(vector<vector<int>>& grid, int x, int y) {
        queue<vector<int>> cells;
        set<pair<int, int>> visited;

        cells.push({x, y, 0});
        vector<pair<int, int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

        while(!cells.empty()) {
            vector<int> cell = cells.front();
            cells.pop();

            pair<int, int> cellPos = make_pair(cell[0], cell[1]);

            if (visited.find(cellPos) != visited.end()) {
                continue;
            }

            visited.insert(cellPos);

            if (grid[cellPos.first][cellPos.second] == 2) {
                return cell[2];
            }

            for (pair<int, int> &direction: directions) {
                pair<int, int> neighborPos = make_pair(
                    cellPos.first + direction.first, 
                    cellPos.second + direction.second
                );
                vector<int> neighbor = {
                    neighborPos.first, 
                    neighborPos.second, 
                    cell[2] + 1
                };

                if (neighbor[0] >= 0 && neighbor[0] < grid.size() 
                    && neighbor[1] >= 0 && neighbor[1] < grid[0].size()
                    && grid[neighbor[0]][neighbor[1]] != 0 
                    && visited.find(neighborPos) == visited.end()
                    ) {
                        cells.push(neighbor);
                    }
            }
        }
        return -1;
    }

public:
    int orangesRotting(vector<vector<int>>& grid) {
        // for each fresh fruit, find its shortest path to a rotten fruit. 
        //return the max value of all shortest paths
        int minimumElapse = -1;
        bool hasFresh = false;

        for (int i = 0; i < grid.size(); ++i) {
            for (int j = 0; j < grid[0].size(); ++j) {
                if (grid[i][j] == 1) {
                    hasFresh = true;
                    int elapse = bfs(grid, i, j);
                    if (elapse == -1) {
                        return -1;
                    }
                    minimumElapse = max(minimumElapse, elapse);
                }
            }
        }

        return hasFresh ? minimumElapse : 0;
    }
};
