class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        
        vector<vector<int>>min_path_sum(grid.size(), vector<int>(grid[0].size(), INT_MAX));

        min_path_sum[0][0] = grid[0][0];
        int min_sum;

        for (auto i = 0; i < grid.size(); i++){
            for (auto j = 0; j < grid[0].size(); j++){
                if(i == 0 && j == 0){
                    continue;
                }

                if (i == 0){
                    min_sum = min_path_sum[i][j-1] + grid[i][j]; 
                }
                else if( j == 0){
                    min_sum = min_path_sum[i-1][j] + grid[i][j];
                }
                else{
                    min_sum = min(min_path_sum[i-1][j], min_path_sum[i][j-1]) + grid[i][j];
                }
                min_path_sum[i][j] = min_sum;

            }
        }

        return min_path_sum[grid.size()-1][grid[0].size()-1];

    }
};