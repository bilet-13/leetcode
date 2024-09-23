class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {

        vector<int> dp(amount+1, -1);

        dp[0] = 0;

        for(const auto& num : coins){
            if(num <= amount){
                dp[num] = 1;
            }
        }

        for(int i = 1 ; i <= amount; i++){
            for(const auto& num : coins){
                if(num <= i &&  dp[i - num] != -1){
                    dp[i] = dp[i] == -1 ? dp[i - num] + dp[num] : min(dp[i], dp[i - num] + dp[num]);
                }
            }
        }
        return dp[amount];
    }
};