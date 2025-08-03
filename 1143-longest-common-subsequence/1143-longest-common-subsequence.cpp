class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        int m = text1.size();
    int n = text2.size();
    // text1 = carbpt, tex2 = cat
    vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0)); // dp[i][j]: the length longest common subsequence
    // of subsequence t1 of text1 (length i) end at text1[i - 1] and sequence
    // t2(length j) end at text2[j - 1] of text2
    // time complexity O(mn) dp[i][j] = dp[i - 1][j - 1] + (text[i -1] == text2[j
    // - 1] ? 1 : 0);

    for (int i = 1; i <= m; ++i) {
      for (int j = 1; j <= n; ++j) {
       if (text1[i - 1] == text2[j - 1]) {
        dp[i][j] = dp[i - 1][j - 1] + 1;
       } else {
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
       }
      }
    }
    return dp[m][n];

    }
};