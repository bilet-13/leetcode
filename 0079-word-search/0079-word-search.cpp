class Solution {
private:
    vector<vector<int>> direction  = {{0,1}, {0, -1}, {1, 0}, {-1, 0}};
    bool _exist(vector<vector<char>>& board, string& word, int i, int x, int y){
        if(i == word.size()){
            return true;
        }

        if(x < 0 || x >= board.size() || y < 0 || y >= board[0].size() || board[x][y] != word[i]){
            return false;
        }

        board[x][y] = '0';

        for(const auto& dir : direction){
            if(_exist(board, word, i+1, x + dir[0], y + dir[1])){
                return true;
            }
        }
        board[x][y] = word[i];
        return false;
    }
public:
    bool exist(vector<vector<char>>& board, string word) {

        for (int i = 0;  i < board.size(); i++){
            for(int j = 0; j < board[0].size(); j++){
                if(_exist(board, word, 0, i, j)){
                    return true;
                }
            }
        }
        return false;
    }
};