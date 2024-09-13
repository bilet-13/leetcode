struct Node{
    unordered_map<char, Node*> childs;
    bool is_end;

    Node(){
        is_end = false;
    }
};
class Trie {
private:
    Node* root;
public:
    Trie() {
        root = new Node();
    }
    
    void insert(string word) {
        auto node = root;
        for(char chr : word){
            if(node->childs.count(chr) == 0){
                node->childs[chr] = new Node();
            }
            node = node->childs[chr];
        }
        node->is_end = true;
    }
    
    bool search(string word) {
        auto node = root;
        for(char chr : word){
            if(node->childs.count(chr) == 0){
                return false;
            }
            node = node->childs[chr];
        }
        return node->is_end;
    }
    
    bool startsWith(string prefix) {
        auto node = root;
        for(char chr : prefix){
            if(node->childs.count(chr) == 0){
                return false;
            }
            node = node->childs[chr];
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