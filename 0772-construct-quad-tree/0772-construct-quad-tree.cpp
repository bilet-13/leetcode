/*
// Definition for a QuadTree node.
class Node {
public:
    bool val;
    bool isLeaf;
    Node* topLeft;
    Node* topRight;
    Node* bottomLeft;
    Node* bottomRight;
    
    Node() {
        val = false;
        isLeaf = false;
        topLeft = NULL;
        topRight = NULL;
        bottomLeft = NULL;
        bottomRight = NULL;
    }
    
    Node(bool _val, bool _isLeaf) {
        val = _val;
        isLeaf = _isLeaf;
        topLeft = NULL;
        topRight = NULL;
        bottomLeft = NULL;
        bottomRight = NULL;
    }
    
    Node(bool _val, bool _isLeaf, Node* _topLeft, Node* _topRight, Node* _bottomLeft, Node* _bottomRight) {
        val = _val;
        isLeaf = _isLeaf;
        topLeft = _topLeft;
        topRight = _topRight;
        bottomLeft = _bottomLeft;
        bottomRight = _bottomRight;
    }
};
*/

class Solution {
private: 
    bool isSameValue(vector<vector<int>>& grid, int i, int j, int w){
        int val = grid[i][j];
        for(int i1 = i; i1 < i+w; i1++){
            for(int j1 = j; j1 < j+w; j1++){
                if(grid[i1][j1] != val){
                    return false;
                }
            }
        }
        return true;
    }

    Node* _construct(vector<vector<int>>& grid, int i, int j, int w){

        if(isSameValue(grid, i, j, w)){
            return new Node((grid[i][j] == 1), true);
        }

        Node* node = new Node();

        int size = w / 2;
        node->topLeft = _construct(grid, i, j, size);
        node->topRight = _construct(grid, i, j + size, size);
        node->bottomLeft = _construct(grid, i + size, j, size);
        node->bottomRight = _construct(grid, i + size, j + size, size);

        node->isLeaf = false;
        return node;    
    }

public:
    Node* construct(vector<vector<int>>& grid) {
        return _construct(grid, 0, 0, grid.size());
    }
};