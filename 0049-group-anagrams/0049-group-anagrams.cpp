class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> anagrams_group;
        vector<vector<string>> answer;

        for (string str : strs){
            string sorted_string = str;
            sort(sorted_string.begin(), sorted_string.end());

            auto iter = anagrams_group.find(sorted_string);
            if(iter != anagrams_group.end()){
                iter->second.push_back(str);
            }

            else{
                vector<string> tmp = {str};
                anagrams_group[sorted_string] = tmp;
            }
        }

        for (auto anagram : anagrams_group){
            answer.push_back(anagram.second);
        }

        return answer;
    }
};