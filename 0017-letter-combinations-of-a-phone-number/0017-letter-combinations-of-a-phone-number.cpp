class Solution {
private:
unordered_map<int, vector<string>> m_num_letters = {
        {2, {"a", "b", "c"}},
        {3, {"d", "e", "f"}},
        {4, {"g", "h", "i"}},
        {5, {"j", "k", "l"}},
        {6, {"m", "n", "o"}},
        {7, {"p", "q", "r", "s"}},
        {8, {"t", "u", "v"}},
        {9, {"w", "x", "y", "z"}}
    };
vector<string> _getChar(string num){
    return m_num_letters[stoi(num)];
}

public:
    vector<string> letterCombinations(string digits) {
        if(digits.size() == 0){
            return {};
        }
        vector<string> combined_letters;
        queue<string> letters_node;
        
        auto root_letters = _getChar(digits.substr(0, 1));
        for(auto letter: root_letters){
            letters_node.push(std::move(letter));
        }

        int len = 0;
        while(!letters_node.empty()){
            if(len == digits.size()-1){
                while(!letters_node.empty()){
                    combined_letters.push_back(letters_node.front());
                    letters_node.pop();
                }
                break;
            }

            len += 1;
            auto next_letters = _getChar(digits.substr(len, 1));
            int size = letters_node.size();

            for(int i = 0; i < size; i++){
                auto node = letters_node.front();
                letters_node.pop();

                for( auto next: next_letters){
                    letters_node.push(node+next);
                }
            }
        }
        return combined_letters;
    }

};