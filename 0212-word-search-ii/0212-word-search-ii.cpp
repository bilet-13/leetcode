#include<algorithm>
class Solution {
private:
    class TreeNode {
        public: 
            TreeNode *child[26];
            bool isEndOfWord = false;

            TreeNode() {
                for (int i = 0; i < 26; ++i) {
                    child[i] = nullptr;
                }
            }
    };

    class Trie {
        private:
            TreeNode *root;
        public:
            Trie() {
                root = new TreeNode();
            }

            void insertWord(string word) {
                auto node = root;

                for (const auto &chr: word) {
                    if (node->child[chr - 'a'] == nullptr) {
                        node->child[chr - 'a'] = new TreeNode();
                    }
                    node = node->child[chr - 'a'];
                }
                node->isEndOfWord = true;
            }

            bool findPrefix(string &word) {
                auto node = root;

                for (const auto &chr: word) {
                    if (node->child[chr - 'a'] == nullptr) {
                        return false;
                    }
                    node = node->child[chr - 'a'];
                }
                return true;
            }

            bool searchWord(string &word) {
                auto node = root;

                for (const auto &chr: word) {
                    if (node->child[chr - 'a'] == nullptr) {
                        return false;
                    }
                    node = node->child[chr - 'a'];
                }
                return node->isEndOfWord;
            }
    };

    void backtrack(int step, int x, int y, vector<vector<char>> &board, Trie *trie, string current, unordered_set<string> &result, const int &longest_step) {
        if (x < 0 || x >= board.size() || y < 0 || y >= board[0].size() || board[x][y] == '#' || step > longest_step) {
            return;
        } 

        const auto chr = board[x][y];

        current.push_back(chr);
        if (!trie->findPrefix(current)) {
            return;
        }
        
        if(trie->searchWord(current)) {
            result.insert(current);
        }

        board[x][y] = '#';

        backtrack(step + 1, x + 1, y, board, trie, current, result, longest_step);
        backtrack(step + 1, x - 1, y, board, trie, current, result, longest_step);
        backtrack(step + 1, x, y + 1, board, trie, current, result, longest_step);
        backtrack(step + 1, x, y - 1, board, trie, current, result, longest_step);

        current.pop_back();
        board[x][y] = chr;
    }
     
public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        Trie *trie = new Trie();
        unordered_set<string> result;
        string current;
        int longest_word_length = -1;

        for (const auto &word : words) {
            int size = word.size();
            longest_word_length = std::max(longest_word_length, size);
            trie->insertWord(word);
        }

        for (int i = 0; i < board.size(); ++i) {
            for (int j = 0; j < board[0].size(); ++j) {
                backtrack(0, i, j, board, trie, current, result, longest_word_length - 1);
            }
        }   

        vector<string> returned_result;

        for (auto word: result) {
            returned_result.push_back(word);
        }

        return returned_result;
    }
};
