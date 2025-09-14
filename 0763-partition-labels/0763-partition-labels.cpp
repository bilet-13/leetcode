class Solution {
public:
    vector<int> partitionLabels(string s) {
        // brute force record each lettter's 
        // positions and group them
        // if a letter  L only appear once it can become substring
        // else the substrint need to be contine all posion of L
        // idea: for loop a string to store the 
        // first and the last posion of each letter, then while loop the string
        // substring s need to contain all first letter and 
        // then continue to check the sub s keep update the sub s by check all letter in the substr

        vector<int> farthest(26, 0);
        int start = 0;
        vector<int> result;

        // O(n) n = s.size()
        for (int i = 0; i < s.size(); ++i) {
            char ch = s[i];
            farthest[ch - 'a'] = max(i, farthest[ch - 'a']);
        }

        //O(n ^ 2)
        while (start < s.size()) {
            string sub = string(1, s[start]);
            int subIdx = 0;

            while (subIdx < sub.size()) {
                int farthestIdx = farthest[sub[subIdx] - 'a'];
                if (farthestIdx > start + sub.size() - 1) {
                    sub = s.substr(start, farthestIdx - start + 1);
                }
                subIdx += 1;
            }

            result.push_back(sub.size());
            start += sub.size();
        }
        return result; // time complexity O()
    }
};
