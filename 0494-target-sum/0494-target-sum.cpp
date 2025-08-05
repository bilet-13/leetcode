
class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        int sum = std::accumulate(nums.begin(), nums.end(), 0);
        vector<vector<int>> dp(nums.size() + 1, vector<int>(2 * sum + 1, 0));
        // the number of way to use the first i elemente to get a sum of j - sum
        dp[0][sum] = 1;
        if (target > sum || target < -sum) {
            return 0;
        }

        for (int i = 1; i <= nums.size(); ++i) {
            int num = nums[i - 1];

            for (int curSum = -sum; curSum <= sum; ++curSum) {
                int j = curSum + sum;

                if (dp[i - 1][j] > 0) {
                    dp[i][j + num] += dp[i - 1][j];
                    dp[i][j - num] += dp[i - 1][j];
                }
            }
        }
        return dp[nums.size()][target + sum];
    }
};
