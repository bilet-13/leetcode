class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> result;
        traverse_four_edges(matrix, result, 0, matrix.size()-1, 0, matrix[0].size()-1);
        return result;
    }

    void traverse_four_edges(vector<vector<int>>& matrix, vector<int>& result, int r_start, int r_end, int c_start, int c_end){
        if(r_start <= r_end && c_start <= c_end){
            for(int i = c_start; i <= c_end; i++){
                result.push_back(matrix[r_start][i]);
            }
            if(r_start < r_end){
                for(int i = r_start+1; i <= r_end; i++){
                    result.push_back(matrix[i][c_end]);
                }
                
                if(c_start < c_end){
                    for(int i = c_end-1; i >= c_start; i--){
                    result.push_back(matrix[r_end][i]);
                    }
                    for(int i = r_end-1; i > r_start; i--){
                        result.push_back(matrix[i][c_start]);
                    }
                }
            }
            traverse_four_edges(matrix, result, r_start+1, r_end-1, c_start+1, c_end-1);
        }
        return;
    }
};

// 00 01 02 12 22 21 20 10 11