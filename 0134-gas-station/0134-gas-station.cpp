class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int totalGas = 0;
        int totalCost = 0;
        int curGas = 0;
        int start = 0;
        int n = gas.size();

        for (int i = 0; i < n; ++i) {
            totalGas += gas[i];
            curGas += gas[i];

            totalCost += cost[i];

            if (curGas < cost[i]) {
                start = i + 1;
            }
            curGas = max(0, curGas - cost[i]);
        }

        return (totalCost > totalGas) ? -1 : start;
    }
};
