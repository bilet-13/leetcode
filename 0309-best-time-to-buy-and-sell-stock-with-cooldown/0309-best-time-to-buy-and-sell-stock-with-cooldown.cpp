class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int m = prices.size();

  vector<int> hold(m); // 
  vector<int> sold(m);
  vector<int> rest(m);

  hold[0] = -prices[0];
  sold[0] = 0;
  rest[0] = 0;

  for (int i = 1; i < m; ++i) {
    hold[i] = max(hold[i - 1], rest[i - 1] - prices[i]);
    sold[i] = hold[i - 1] + prices[i];
    rest[i] = max(rest[i - 1], sold[i - 1]);
  }

  return max(sold[m - 1], rest[m - 1]);
    }
};
