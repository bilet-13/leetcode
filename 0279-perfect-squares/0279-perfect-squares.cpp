class Solution {
public:
    int numSquares(int n) {
        vector<int> dp_table(n+1, INT_MAX);
        dp_table[0] = 0;
        dp_table[1] = 1;

        for(auto i = 1; i*i <= n; i++){
            dp_table[i*i] = min(dp_table[i*i], 1);
        }

        for(auto i = 2; i <= n; i++){
            for(auto j = 1; j <= i; j++ ){
                dp_table[i] = min(dp_table[i], dp_table[i-j] + dp_table[j]);
            }
        }
        return dp_table[n];
    }
};