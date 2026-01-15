
class Trie {
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

private:
    TreeNode *root;
public:
    Trie() {
        root = new TreeNode();
    }
    
    void insert(string word) {
        auto node = root;

        for(const auto &chr: word) {
            if (node->child[chr - 'a'] == nullptr) {
                node->child[chr - 'a'] = new TreeNode();
            }
            node = node->child[chr - 'a'];
        }
        node->isEndOfWord = true;
    }
    
    bool search(string word) {
        auto node = root;

        for(const auto &chr: word) {
            if (node->child[chr - 'a'] == nullptr) {
                return false;
            }
            node = node->child[chr - 'a'];
        }
        return node->isEndOfWord;
    }
    
    bool startsWith(string prefix) {
         auto node = root;

        for(const auto &chr: prefix) {
            if (node->child[chr - 'a'] == nullptr) {
                return false;
            }
            node = node->child[chr - 'a'];
        }
        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */