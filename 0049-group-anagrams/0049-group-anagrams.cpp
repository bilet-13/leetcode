class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> anagrams_group;
        vector<vector<string>> answer;

        for (const string& str : strs){
            string sorted_string = str;
            sort(sorted_string.begin(), sorted_string.end());

            anagrams_group[sorted_string].push_back(str);
        }

        for (const auto& anagram : anagrams_group){
            answer.push_back(move(anagram.second));
        }

        return answer;
    }
};