class Solution {
public:
    int climbStairs(int n) {
        if (n==1){
            return 1;
        }
        vector<int> dp_climbings(n+1, 0);
        dp_climbings[1] = 1;
        dp_climbings[2] = 2;
        
        for (auto i = 3; i <= n; i++ ) {
            dp_climbings[i] = dp_climbings[i-1] + dp_climbings[i-2];
        }

        return dp_climbings[n];
    }
};