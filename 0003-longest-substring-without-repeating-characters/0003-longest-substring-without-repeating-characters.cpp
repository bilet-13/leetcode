class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> prev_chars;
        int w_size = 0;
        int max_len = 0;

        for(int i = 0; i < s.size(); i++){
            if(i > 0){
                prev_chars.erase(s[i-1]);
                w_size--;
            }

            while(i+w_size < s.size() && prev_chars.count(s[i+w_size]) == 0){
                prev_chars.insert(s[i+w_size]);
                w_size++;
            }
            max_len = max(max_len, w_size);
        }
        return max_len;
    }
};