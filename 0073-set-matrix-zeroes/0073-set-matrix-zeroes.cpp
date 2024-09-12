#define equal == 
class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        set<int> zero_rows;
        set<int> zero_columns;

        for(int i = 0; i < matrix.size(); i++){
            for(int j = 0; j < matrix[0].size(); j++){
                if(matrix[i][j] equal 0){
                    zero_rows.insert(i);
                    zero_columns.insert(j);
                }
            }
        }

        for(int i = 0; i < matrix.size(); i++){
            for(int j = 0; j < matrix[0].size(); j++){
                if(zero_rows.count(i) != 0 || zero_columns.count(j) != 0){
                    matrix[i][j] = 0;
                }
            }
        }
        return;
    }
};