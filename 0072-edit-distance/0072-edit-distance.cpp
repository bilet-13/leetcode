class Solution {
public:
    int minDistance(string word1, string word2) {
        int n = word1.size();
        int m = word2.size();
        vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0)); 
        // dp[i][j]: the minimum number of ops to let the string consiti of 
        // first i char of word1 equal to the string consist of the first j char of word2
        for (int i = 0; i <= n; ++i) {
            dp[i][0] = i;
        }

        for (int j = 0; j <= m; ++j) {
            dp[0][j] = j;
        }

        for (int i = 1; i <=n; ++i) {
            for (int j = 1; j <= m; ++j) {
                if (word1[i - 1] == word2[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    vector<int> candidates = {dp[i - 1][j - 1] + 1, dp[i - 1][j] + 1, dp[i][j - 1] + 1};
                    // candidates:1 replace word1[i -1] to word2[j - 1 ], 2 deleta a char then do operation that make first i - 1 char to first j char, 3 after an operation that make first i char to j - char and then insert a char
                    dp[i][j] = *min_element(candidates.begin(), candidates.end());
                }
            }
        }

        return dp[n][m];
    }
};
