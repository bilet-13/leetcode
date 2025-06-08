class Solution {
private:
    unordered_map<int, string> num_letters = {
        {2, "abc"}, 
        {3, "def"}, 
        {4, "ghi"}, 
        {5, "jkl"}, 
        {6, "mno"},
        {7, "pqrs"},
        {8, "tuv"},
        {9, "wxyz"}
    };

    void backtrack(int step, string &digits, string current, vector<string> &result) {
        if (step == digits.size() && current.size() > 0) {
            result.push_back(current);
            return;
        }

        string letters = num_letters[digits[step] - '0'];

        for(int i = 0; i < letters.size(); ++i) {
            current.push_back(letters[i]);

            backtrack(step + 1, digits, current, result);

            current.pop_back();
        }
    }

public:
    vector<string> letterCombinations(string digits) {
        vector<string> result;
        string current;

        backtrack(0, digits, current, result);

        return result;
    }
};
