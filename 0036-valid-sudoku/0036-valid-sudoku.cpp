class Solution {
private:
    const int sub_size = 3;
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        bool answer = true;

        for(int i = 0; i < board.size(); i++){
            answer = answer && isValidRow(board, i);
            answer = answer && isValidColumn(board, i);

            if(!answer){
                return answer;
            }
        }

        for(int i = 0; i < board.size(); i += 3){
            for (int j = 0; j < board.size(); j += 3){
                answer = answer && isValidSubBox(board, i, j);
            }
        }
        return answer;
    }

    bool isValidRow(vector<vector<char>>& board, int row){
        unordered_map<char, bool> nums;
        for(int column = 0; column < board.size(); column++){
            // if(board[row][column] < 0 || board[row][column] > 9){
            //     return false;
            // }
            if (board[row][column] == '.') continue;

            auto iter = nums.find(board[row][column]);
            if(iter != nums.end()){
                return false;
            }

            nums[board[row][column]] = true;
        }
        return true;
    }

    bool isValidColumn(vector<vector<char>>& board, int column){
        unordered_map<char, bool> nums;
        for(int row = 0; row < board.size(); row++){
            // if(board[row][column] < 0 || board[row][column] > 9){
            //     return false;
            // }
            if (board[row][column] == '.') continue;

            auto iter = nums.find(board[row][column]);
            if(iter != nums.end()){
                return false;
            }

            nums[board[row][column]] = true;
        }
        return true;
    }

    bool isValidSubBox(vector<vector<char>>& board, int row_start, int column_start){
        unordered_map<char, bool> nums;
        for(int i = row_start; i < row_start+3; i++){
            for(int j = column_start; j < column_start+3; j++){
                // if (board[i][j] < 0 || board[i][j] > 9){
                //     return false;
                // }
                if (board[i][j] == '.') continue;

                auto iter = nums.find(board[i][j]);
                if(iter != nums.end()){
                    return false;
                }

                nums[board[i][j]] = true;
            }
            
        }
        return true;
    }

};