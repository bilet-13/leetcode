class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        // simulate the four direction way travsal
        int m = matrix.size();
        int n = matrix[0].size();
        vector<int> orderResult;

        int top = 0;
        int end = m - 1;
        int left = 0;
        int right = n - 1;

        while (left <= right && top <= end) {
            for (int i = left; i <= right; ++i) {
                orderResult.push_back(matrix[top][i]);
            }
            top++;

            if (left > right || top > end) {
                break;
            }

            for (int i = top; i <= end; ++i) {
                orderResult.push_back(matrix[i][right]);
            }
            right--;

            if (left > right || top > end) {
                break;
            }

            for (int i = right; i >= left; --i) {
                orderResult.push_back(matrix[end][i]);
            }
            end--;

            if (left > right || top > end) {
                break;
            }

            for (int i = end; i >= top; --i) {
                orderResult.push_back(matrix[i][left]);
            }
            left++;
        }

        return orderResult;
    }
};
