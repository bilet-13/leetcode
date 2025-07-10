class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }

        vector<int> sCount(26, 0);
        vector<int> tCount(26, 0);

        for (int i = 0; i < s.size(); ++i) {
            sCount[s[i] - 'a']++;
            tCount[t[i] - 'a']++;
        }

        return sCount == tCount;
    }
};
