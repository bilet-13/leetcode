class Solution {
public:
    int maxProfit(vector<int>& prices) {
        vector<int> max_sell_prices(prices.size(), 0);
        int max_price = 0;
        int max_profit = 0;

        for(int i = prices.size()-1; i > -1; i--){
            max_sell_prices[i] = max_price;
            cout<<max_price;
            max_price = max(max_price, prices[i]);
        }

        for (auto i = 0; i < prices.size(); i++ ){
            int profit = max(0, max_sell_prices[i]-prices[i]);
            max_profit = max(max_profit, profit);
        }
        return max_profit;
    }
};