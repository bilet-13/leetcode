class Solution {
private:
    bool isSafe(pair<int, int> pos, vector<pair<int, int>>& queens) {
    for (const auto& queen : queens) {
        int rowQ = queen.first;
        int colQ = queen.second;
        
        int row = pos.first;
        int col = pos.second;
        
        // Check if they are in the same column
        if (col == colQ) {
            return false;
        }
        
        int dy = col - colQ;
        int dx = row - rowQ;
        if ( abs(dx) == abs(dy)) {
            return false;
        }
    }
    
    // If no conflicts, the position is safe
    return true;
}

    int _findQueens(int n, int row, vector<pair<int, int>>& queens){
        if(queens.size() == n){
            return 1;
        }

        int count = 0;

        for(int column = 0; column < n; column++){
            pair<int, int> pos = {row, column};
            if(isSafe(pos, queens)){
                queens.push_back(pos);
                count += _findQueens(n, row+1, queens);
                queens.pop_back();
            }
        }
        return count;
    }
public:
    int totalNQueens(int n) {
        if (n == 1){
            return 1;
        }

        vector<pair<int, int>> queens;
        return _findQueens(n, 0, queens);
    }
};