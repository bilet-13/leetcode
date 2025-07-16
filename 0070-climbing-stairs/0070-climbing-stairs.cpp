class Solution {
public:
    int climbStairs(int n) {
        // i(n) = i(n-1) + i(n-2) 
        if (n < 3) {
            return n;
        }

        int prev1 = 1;
        int prev2 = 2;
        int step;

        for (int i = 3; i <= n; ++i) {
            int tmpPrev = prev2;

            step = prev1 + prev2;
            prev2 = step;
            prev1 =  tmpPrev;
        }
        return step;
    }
};
