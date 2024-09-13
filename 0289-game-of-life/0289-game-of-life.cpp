class Solution {
    
public:
    void gameOfLife(vector<vector<int>>& board) {
        for(int i = 0 ; i < board.size() ;i++){
            for (int j = 0 ; j < board[0].size(); j++){
                int live_neighbor = getLiveNeighbor(board, i , j);
                if (live_neighbor == 3 && board[i][j] == 0)board[i][j] = 5;
                else if(live_neighbor < 2 && board[i][j] == 1) board[i][j] = 2;
                else if(live_neighbor > 3 && board[i][j] == 1) board[i][j] = 4;
                else if(board[i][j] == 1) board[i][j] = 3;
            }
        }
        for(int i = 0 ; i < board.size() ;i++){
            for (int j = 0 ; j < board[0].size(); j++){
                if (board[i][j] == 2)board[i][j] = 0;
                else if(board[i][j] == 3) board[i][j] = 1;
                else if(board[i][j] == 4) board[i][j] = 0;
                else if(board[i][j] == 5) board[i][j] = 1;
            }
        }
    }

    bool isLive(vector<vector<int>>& board, int i, int j){
        if(i >= 0 && i < board.size() && j >= 0 && j < board[0].size()){
            return (board[i][j] == 1 || board[i][j] == 2 || board[i][j] == 3 || board[i][j] == 4);
        }
        return false;
    }
    int getLiveNeighbor(vector<vector<int>>& board, int i, int j){
        int neighbor = 0;
        
        if(isLive(board, i-1, j-1)) neighbor++;
        if(isLive(board, i-1, j)) neighbor++;
        if(isLive(board, i-1, j+1)) neighbor++;

        if(isLive(board, i, j-1)) neighbor++;
        if(isLive(board, i, j+1)) neighbor++;
        
        if(isLive(board, i+1, j-1)) neighbor++;
        if(isLive(board, i+1, j)) neighbor++;
        if(isLive(board, i+1, j+1)) neighbor++;

        return neighbor;
    }
};