class Solution {
private:
    bool isValid(int row, int col, const vector<string> &board) {
         int n = board.size();
    
    // check same column
    for (int i = 0; i < row; ++i)
        if (board[i][col] == 'Q')
            return false;

    // check upper-left diagonal
    for (int i = row - 1, j = col - 1; i >= 0 && j >= 0; --i, --j)
        if (board[i][j] == 'Q')
            return false;

    // check upper-right diagonal
    for (int i = row - 1, j = col + 1; i >= 0 && j < n; --i, ++j)
        if (board[i][j] == 'Q')
            return false;

        return true;
    }

    void backtrack(vector<string> board, vector<vector<string>> &result, int row, int n) {
        if (row == n) {
            result.push_back(board);
            return;
        }

        
            for (int j = 0; j < board[0].size(); ++j) {
                if (isValid(row, j, board)) {
                    board[row][j] = 'Q';

        
                    backtrack(board, result, row + 1, n);

                    board[row][j] = '.';
                }
            }
        
    }

public:
    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>> result;

        vector<string> board = vector<string>(n, string(n, '.'));

        backtrack(board, result, 0, n);

        return result;
    }
};
