class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> s_count;

        if(s.size() > t.size()){
            swap(s, t);
        }
        
        for (char chr : s){
            auto iter = s_count.find(chr);

            if(iter == s_count.end()){
                s_count[chr] = 0;
            }
            s_count[chr] += 1;
        }

        for (char chr : t){
            auto iter = s_count.find(chr);

            if(iter == s_count.end() || iter->second == 0){
                return false;
            }

            iter->second -= 1;
        }
        return true;
    }
};