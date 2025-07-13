class Solution {
public:
    bool isPalindrome(string s) {
        int start = 0;
        int end = s.size() - 1;

        while (start < end) {
            if (!std::isalnum(s[start])) {
                start++;
                continue;
            } else if (!std::isalnum(s[end])) {
                end--;
                continue;
            }
            
            if (std::tolower(s[start++]) != std::tolower(s[end--])) {
                return false;
            }
        }
        return true;
    }
};
