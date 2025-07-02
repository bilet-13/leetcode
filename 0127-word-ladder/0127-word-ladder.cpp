class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        // shortest bath problem between beginWord and endWord
        // each word is a node in graph 
        // word a can transofro to word b => a -> b
        // build the graph with 0: beginword 1 - n word in wordList
        int n = wordList.size();
        vector<vector<int>> graph(n + 1);
        vector<bool> visited(n + 1, false);
        queue<pair<int, int>> q;

        // time complexity o(N^2L) // L = word length
        for (int i = 0; i <= n; ++i) {
            auto& cur = (i == 0) ? beginWord : wordList[i - 1];

            for (int k = 0; k < n; ++k) {
                auto& word = wordList[k];
                int diffNum = 0;

                for (int j = 0; j < word.size(); ++j) {
                    diffNum += cur[j] != word[j] ? 1 : 0;
                }
                if (diffNum == 1) {
                    graph[i].push_back(k + 1);
                }
            }
        }

        q.emplace(0, 1);
        while (!q.empty()) {
            auto [node, step] = q.front();
            q.pop();

            if (visited[node]) {
                continue;
            }
            visited[node] = true;

            auto& cur = (node == 0) ? beginWord : wordList[node - 1];
            if (cur == endWord) {
                return step;
            }

            for (auto &neighbor: graph[node]) {
                if (!visited[neighbor]) {
                    q.emplace(neighbor, step + 1);
                }
            }
        }
        // do bfs return the shorstest path between beginWord and endWord else retun 0
        return 0;
    }
};
