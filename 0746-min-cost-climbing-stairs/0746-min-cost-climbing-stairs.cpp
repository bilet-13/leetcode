class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int n = cost.size();
        vector<int> totalCost(n + 1, INT_MAX);
        totalCost[0] = 0;
        totalCost[1] = 0;

        for (int i = 2; i <= n; ++i) {
            totalCost[i] = min(totalCost[i - 1] + cost[i - 1], totalCost[i - 2] + cost[i - 2]);
        }
        return totalCost[n];
    }
};
