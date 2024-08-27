class Solution {
public:
    int numSquares(int n) {
        vector<int> dp_table(n+1, INT_MAX);
        dp_table[0] = 0;
        
        
        for(auto i = 1; i <= n; i++){
            for(auto j = 1; j*j <= i; j++ ){
                dp_table[i] = min(dp_table[i], dp_table[i-j*j] + 1);
            }
        }
        return dp_table[n];
    }
};