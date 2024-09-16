class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        
        unordered_set<string> words(wordList.begin(), wordList.end());
        queue<pair<string, int>> nodes;
        unordered_set<string> visited;

        nodes.push({beginWord, 1});
        visited.insert(beginWord);

        while(!nodes.empty()){
            auto cur = nodes.front();
            nodes.pop();

            if(cur.first == endWord){
                return cur.second;
            }

            string cur_word = cur.first;
            for(int i = 0; i < cur_word.size(); i++){
                char cur_char = cur_word[i];

                for(int j = 0; j < 26; j++){
                    if(cur_char != static_cast<char>('a'+j)){
                        cur_word[i] = static_cast<char>('a'+j);
                        if(words.count(cur_word) != 0 && visited.count(cur_word) == 0){
                            nodes.push({cur_word, cur.second+1});
                            visited.insert(cur_word);
                        }
                        cur_word[i] = cur_char;
                    }
                }
            }    
        }
        return 0;
    }
};