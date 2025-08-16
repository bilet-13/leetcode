class Solution {
public:
    bool isMatch(string s, string p) {
        return matchHelper(s, p, 0, 0);
    }

    bool matchHelper(string& s, string& p, int i, int j) {
        if (j == p.size()) {
            return i == s.size();
        } 

        bool firstMatch = (i < s.size() && (s[i] == p[j] || p[j] == '.'));

        if (j + 1 < p.size() && p[j + 1] == '*') {
            return matchHelper(s, p, i, j + 2) || (firstMatch && matchHelper(s, p, i + 1, j));
        } else {
            return firstMatch && matchHelper(s, p, i + 1, j + 1);
        }
    }
};