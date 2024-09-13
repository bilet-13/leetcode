class Solution {
    
public:
    void gameOfLife(vector<vector<int>>& board) {
        for(int i = 0 ; i < board.size() ;i++){
            for (int j = 0 ; j < board[0].size(); j++){
                int neighbor = getLiveNeighbor(board, i , j);
                if (neighbor == 3 && board[i][j] == 0)board[i][j] = 5;
                else if(neighbor < 2 && board[i][j] == 1) board[i][j] = 2;
                else if(neighbor > 3 && board[i][j] == 1) board[i][j] = 4;
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
        return (board[i][j] == 1 || board[i][j] == 2 || board[i][j] == 3 || board[i][j] == 4);
    }
    int getLiveNeighbor(vector<vector<int>>& board, int i, int j){
        int neighbor = 0;
        if (i - 1 >= 0){
            if(j-1 >= 0 && isLive(board, i-1, j-1)) neighbor++;
            if(isLive(board, i-1, j)) neighbor++;
            if(j+1 < board[0].size() && isLive(board, i-1, j+1)) neighbor++;
        }

        if(j-1 >= 0 && isLive(board, i, j-1)) neighbor++;
        if(j+1 < board[0].size() && isLive(board, i, j+1)) neighbor++;

        if (i + 1 < board.size()){
            if(j-1 >= 0 && isLive(board, i+1, j-1)) neighbor++;
            if(isLive(board, i+1, j)) neighbor++;
            if(j+1 < board[0].size() && isLive(board, i+1, j+1)) neighbor++;
        }
        return neighbor;
    }
};