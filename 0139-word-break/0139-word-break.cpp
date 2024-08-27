class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        vector<bool> is_string_segemented(s.length()+1, false);
        is_string_segemented[0] = true;

        for(auto i = 1; i <= s.length(); i++){
            for(auto iter = wordDict.begin(); iter != wordDict.end(); iter++){
                if(i >= iter->length()  && s.substr(i - iter->length(), iter->length()) == *iter){
                    is_string_segemented[i] =  is_string_segemented[i] || is_string_segemented[i - iter->length()];
                }
            }
        }

        return is_string_segemented[s.length()];
    }
};