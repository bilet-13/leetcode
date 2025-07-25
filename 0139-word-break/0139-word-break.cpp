class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        int n = s.size();
        vector<bool> dp(s.size() + 1); // dp[i] : the string s[0:i - 1] can be segemented by words in word dict or not
        dp[0] = true;

        for (int i = 1; i <= n; ++i) {
            for (const auto& word : wordDict) {
                int idx = i - word.size(); 
                if (idx >= 0 && idx < n) {
                    dp[i] = dp[i] ||(dp[i - word.size()] &&  word == s.substr(idx, word.size()));
                }
            }
        }

        return dp[s.size()]; // n: s.size(), d: wordDict.size(), w: max word.size() O(ndw);
        //  permutation d^d  brute force
    }
};
