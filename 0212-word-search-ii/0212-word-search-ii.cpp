struct Node{
    unordered_map<char, Node*> child;
    bool is_word;

    Node(): is_word(false){
    }
};

class Solution {

private:
    Node* root;

    void _addWord(string word){
        auto cur = root;
        for(const auto& chr: word){
            auto iter = cur->child.find(chr);
            if(iter == cur->child.end()){
                cur->child[chr] = new Node();
            }
            cur = cur->child[chr];
        }
        cur->is_word = true;
    }

    void _DFS(Node* node, unordered_set<string>& result, vector<vector<char>>& board, vector<vector<bool>>& visited, string& cur, int i, int j){
        vector<pair<int, int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        
        int m = board.size();
        int n = board[0].size();

        auto iter = node->child.find(board[i][j]);
        if(iter == node->child.end()){
            return;
        }
        
        node = iter->second;
        cur.push_back(board[i][j]);

        if(node->is_word){
            result.insert(cur);
        }

        for(auto& d : directions){
            auto nx = i + d.first;
            auto ny = j + d.second;

            if(0 <= nx && nx < m && 0 <= ny && ny < n && !visited[nx][ny]){
                auto it = node->child.find(board[nx][ny]);
                if(it != node->child.end()){
                    visited[nx][ny] = true;
                    _DFS(node, result, board, visited, cur, nx, ny);
                    visited[nx][ny] = false;
                }                
            }

        }
        cur.pop_back();
    }
public:
    Solution(){
        root = new Node();
    }
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        
        int m = board.size();
        int n = board[0].size();
        unordered_set<string> found_words;
        
        for(const auto& word: words){
            _addWord(word);
        }

        for(int i = 0; i < m; i++){
            for(int j = 0; j < n ; j++){
                vector<vector<bool>> visited(m, vector<bool>(n, false));
                visited[i][j] = true;
                string start ;
                _DFS(root, found_words, board, visited, start, i, j);
            
            }
        }
        
        return vector<string>(found_words.begin(), found_words.end());
    }

};