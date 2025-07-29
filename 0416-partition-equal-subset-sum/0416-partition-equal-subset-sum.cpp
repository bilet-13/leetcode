#include <numeric>
class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int sum = 0;
        for (const auto& num : nums) {
            sum += num;
        }

        if (sum % 2 == 1) {
            return false;
        }
        int halfSum = sum / 2;
        vector<bool> dp(halfSum + 1, false);
        dp[0] = true;

        for (const auto& num : nums) {
            for (int i = halfSum; i >= num; --i) {
                dp[i] = dp[i] || dp[i - num];
            }
        }

        return dp[halfSum];
    }
};
