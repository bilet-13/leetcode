class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        vector<bool> is_string_segmented(s.length()+1, false);
        is_string_segmented[0] = true;

        for(auto i = 1; i <= s.length(); ++i){
            for(const string& word : wordDict){
                auto word_len = word.length();

                if(i >= word_len  && s.substr(i - word_len, word_len) == word){
                    is_string_segmented[i] =  is_string_segmented[i] || is_string_segmented[i - word_len];
                }
            }
        }

        return is_string_segmented[s.length()];
    }
};