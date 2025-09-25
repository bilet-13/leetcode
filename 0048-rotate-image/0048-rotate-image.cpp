class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();

        // flip matrix by its diagonal
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < i; ++j) {
                swap(matrix[i][j], matrix[j][i]);
            }   
        }

        // flip matrix by straight line
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < int(n / 2); ++j) {
                swap(matrix[i][j], matrix[i][n - j - 1]);
            }
        }
        return;
    }
};
