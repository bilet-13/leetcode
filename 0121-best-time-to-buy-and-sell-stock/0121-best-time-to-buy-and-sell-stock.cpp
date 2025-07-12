class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int result = 0;
        int minElementToEnd = INT_MAX;

        for (int end = 0; end < prices.size(); ++end) {
            minElementToEnd = min(prices[end], minElementToEnd);
            result = max(prices[end] - minElementToEnd, result);
        } 
        return result;
    }
};
