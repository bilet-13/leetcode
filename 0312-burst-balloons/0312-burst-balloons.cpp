class Solution {
public:
    int maxCoins(vector<int>& nums) {
        int n = nums.size();
        int m = n + 2;
        vector<int> vals(m, 1);
        vector<vector<int>> dp(m, vector<int>(m, 0));

        for (int i = 0; i < n; ++i) {
            vals[i + 1] = nums[i];
        }

        for (int len = 2; len < m; ++len) {
            for (int l = 0; l + len < m; ++l) {
                int r = l + len;
                for (int k = l + 1; k < r; ++k) {
                    dp[l][r] = max(dp[l][r], dp[l][k] + vals[l] * vals[k] * vals[r] + dp[k][r]);
                }
            }
        }

        return dp[0][m - 1];
    }
};
