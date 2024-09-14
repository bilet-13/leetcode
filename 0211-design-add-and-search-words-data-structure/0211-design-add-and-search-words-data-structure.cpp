struct Node{
    unordered_map<char, Node*> child;
    bool is_word;

    Node(){
        is_word = false;
    }
};

class WordDictionary {
private:
    Node* root;

    bool _dfs(Node* root, string word, int i){
        if(i == word.size()){
            return root->is_word;
        }

        if(i >= 0 && i < word.size()){
            if(word[i] != '.'){
                if(root->child.count(word[i]) != 0){
                    return _dfs(root->child[word[i]], word, i+1);
                }
                return false;
            }
            else{
                for(auto node : root->child){
                    if( _dfs(node.second, word, i+1)){
                        return true;
                    }
                }
                return false;
            }
        }
        return false;
    }
public:
    WordDictionary() {
        root = new Node();
    }
    
    void addWord(string word) {
        auto node = root;

        for(char chr : word){
            if(node->child.count(chr) == 0){
                node->child[chr] = new Node(); 
            }
            node = node->child[chr];
        }

        node->is_word = true;
    }
    
    bool search(string word) {
        return _dfs(root, word, 0);
    }
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary* obj = new WordDictionary();
 * obj->addWord(word);
 * bool param_2 = obj->search(word);
 */