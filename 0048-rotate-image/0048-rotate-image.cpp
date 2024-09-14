class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        for(int i = 0; i < matrix.size(); i++){
            int left = 0;
            int right = matrix.size()-1;

            while(left < right){
                swap(matrix[left][i], matrix[right][i]);
                left++;
                right--;
            }
        }
        for(int i = 0; i < matrix.size(); i++){
            for(int j = 0; j < i; j++){
                swap(matrix[i][j], matrix[j][i]);
            }
        }
    }
};