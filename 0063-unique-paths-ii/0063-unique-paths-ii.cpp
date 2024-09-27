class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int m = obstacleGrid.size();
        int n = obstacleGrid[0].size();

        vector<vector<int>> dp(m, vector<int>(n, 0));
        if(obstacleGrid[0][0] != 1){
            dp[0][0] = 1;
        }

        for(int i = 0; i < obstacleGrid.size(); i++){
            for (int j = 0; j < obstacleGrid[0].size(); j++){
                if(i == 0 && j == 0){
                    continue;
                }
                if(obstacleGrid[i][j] != 1){
                    int unique_path = 0;
                    if(i - 1 >= 0){
                        unique_path += dp[i-1][j];
                    }
                    if(j - 1 >= 0){
                        unique_path += dp[i][j-1];
                    }
                    dp[i][j] = unique_path;
                }
            }
        }
        return dp[m-1][n-1];
    }
};