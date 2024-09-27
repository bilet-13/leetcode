class Solution {
public:
    int findMaximizedCapital(int k, int w, vector<int>& profits, vector<int>& capital) {
        vector<pair<int, int>> capital_profits;

        for(int i = 0; i < profits.size(); i++){
            capital_profits.push_back({capital[i], profits[i]});
        }

        sort(capital_profits.begin(), capital_profits.end());

        int index = 0;
        priority_queue<int> net_profits;

        while(k > 0){
            
            while(index < capital_profits.size() && capital_profits[index].first <= w){
                net_profits.push(capital_profits[index].second);
                index++;
            }

            if(net_profits.empty()){
                break;
            }

            w += net_profits.top();
            net_profits.pop();

            k--;
        }
        return w;
    }
};