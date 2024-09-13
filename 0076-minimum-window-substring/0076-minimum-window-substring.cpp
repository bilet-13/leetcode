class Solution {
public:
    string minWindow(string s, string t) {
        unordered_map<char, int> chars;
        for(char c: t){
            if(chars.find(c) == chars.end()) chars[c] = 0;
            chars[c] += 1;
        }

        int left = 0;
        int right = 0;
        int min_len = INT_MAX;
        int start = 0;
        int count = 0;

        while( right < s.size()){
            if (chars.find(s[right]) != chars.end() ){
                chars[s[right]]--;
                if(chars[s[right]] >= 0) count++;
            }

            while(count == t.size()){
                min_len = min(right-left+1, min_len);
                start = min_len == right-left+1 ? left : start;
                if(chars.find(s[left]) != chars.end()){
                    chars[s[left]]++;
                    if(chars[s[left]] > 0) count--;
                }
                left++;
            }
            right++;
        }

        return min_len == INT_MAX ? "" : s.substr(start, min_len);
    }

};