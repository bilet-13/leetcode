class Solution {
public:
    int countSubstrings(string s) {
        // for each char c in s, use c as center 
        int result = 0;
        auto expand = [&](int left, int right) {
            while (left >= 0 && right < s.size()) {
                if (s[left--] != s[right++]) {
                    return;
                }
                result++;
            }
        };

        for (int i = 0; i < s.size(); ++i) {
            result++;// center char is palidrome
            expand(i - 1, i + 1); // odd length
            expand(i, i + 1); // even length
        }

        return result; // O(n ^ 2)
    }
};
