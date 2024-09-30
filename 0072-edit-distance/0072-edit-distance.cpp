class Solution {
public:
    int minDistance(string word1, string word2) {
        vector<vector<int>> dp(word1.size()+1, vector<int>(word2.size()+1,INT_MAX));

        for(int i = 0; i <= word1.size(); i++){
            dp[i][0] = i;
        }
        
        for(int j = 0; j <= word2.size(); j++){
            dp[0][j] = j;
        }

        for(int i = 1; i <= word1.size(); i++){
            for(int j = 1; j <= word2.size(); j++){
                if(word1[i-1] == word2[j-1]){
                    dp[i][j] = dp[i-1][j-1];
                }

                else{
                    int del_cost = dp[i-1][j] + 1;
                    int insert_cost = dp[i][j-1] + 1;
                    int replace_cost = dp[i-1][j-1] + 1;
                    
                    dp[i][j] = (del_cost < insert_cost && del_cost < replace_cost) ? del_cost : (insert_cost < replace_cost) ? insert_cost : replace_cost; 
                }
            }
        }

        return dp[word1.size()][word2.size()];

    }
};