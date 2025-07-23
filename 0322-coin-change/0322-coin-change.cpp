class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        // dp 
        // coins: 1, 5, 10 dp[i] = min(dp[i - 1], dp[i - 5], dp[i - 10]) + 1
        vector<int> dp(amount + 1, INT_MAX); // dp[i]: the fewest number of coins to make up i
        dp[0] = 0;
        
        for (const auto& coin : coins) {
            if (coin <= amount) {
                dp[coin] = 1;
            }
        }

        for (int i = 1; i <= amount; ++i) {
            int numCoins = INT_MAX;
            
            for (const auto& coin : coins) {
                if (i - coin >= 0 && i - coin <= amount) {
                    numCoins = min(numCoins, dp[i - coin]);
                }
            }
            if (numCoins == INT_MAX) {
                continue;
            }

            dp[i] = min(dp[i], numCoins + 1);
        }
        return dp[amount] == INT_MAX ? -1 : dp[amount];
    }
};
