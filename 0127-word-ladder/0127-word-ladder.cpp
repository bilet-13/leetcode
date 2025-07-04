class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        // shortest bath problem between beginWord and endWord
        // each word is a node in graph 
        // word a can transofro to word b => a -> b
        // build the graph with 0: beginword 1 - n word in wordList 
        int n = wordList.size();
        unordered_set<string> words(wordList.begin(), wordList.end());
        if (!words.count(endWord)) {
            return 0;
        }
        unordered_set<string> visited;
        queue<pair<string, int>> q;

        q.emplace(beginWord, 1);
        while (!q.empty()) {
            auto [word, step] = q.front();
            q.pop();

            if (visited.count(word)) {
                continue;
            }
            visited.insert(word);

            if (endWord == word) {
                return step;
            }

            for (int i = 0; i < word.size(); ++i) {
                auto origin = word[i];

                for (char chr = 'a'; chr <= 'z'; chr++) {
                    if (origin == chr) {
                        continue;
                    }
                    word[i] = chr;
                    if (!visited.count(word) && words.count(word)) {
                        words.erase(word);
                        q.emplace(word, step + 1);
                    }
                }
                word[i] = origin;
            }
        }
        return 0;
    }
};
