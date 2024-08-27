class Solution {
public:
    string longestPalindrome(string s) {
        string answer = "";
        int logest = 0;
        int logest_left = 0;
        int logest_right = 0;
        int cur_num = 0;
        int left;
        int right;

        for (auto i = 0; i < s.size(); i++){
            left = i - 1;
            right = i + 1;
            cur_num = 1;
            while(left >= 0 && right < s.size() && s[left] == s[right]){
                cur_num += 2;
                left--;
                right++;
            }

            if (cur_num > logest){
                logest = cur_num;
                logest_left = ++left;
                logest_right = --right;
            }
        }
        for (auto i = 0; i < s.size(); i++){
            left = i;
            right = i + 1;
            cur_num = 0;
            while(left >= 0 && right < s.size() && s[left] == s[right]){
                cur_num += 2;
                left--;
                right++;
            }

            if (cur_num > logest){
                logest = cur_num;
                logest_left = ++left;
                logest_right = --right;
            }
        }

        return s.substr(logest_left, logest_right-logest_left+1);
    }
};