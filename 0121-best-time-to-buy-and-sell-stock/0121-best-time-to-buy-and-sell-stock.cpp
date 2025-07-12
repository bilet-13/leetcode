class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxProfit = 0;
        int minPrice = INT_MAX;

        for (const auto& price : prices) {
            minPrice = min(price, minPrice);
            maxProfit = max(price - minPrice, maxProfit);
        } 
        return maxProfit;
    }
};
