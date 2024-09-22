class Solution {
public:
    long long maximumImportance(int n, vector<vector<int>>& roads) {
        
        vector<int> degree(n, 0);
        long long int max_importance = 0;

        for(const auto& road : roads){
            auto city_a = road[0];
            auto city_b = road[1];

            degree[city_a] += 1;
            degree[city_b] += 1;
        }

        sort(degree.begin(), degree.end(), [](const int a, const int b){return a > b;});

        for(int i = n ; i >= 1; i--){
            max_importance += static_cast<long long>(i) * static_cast<long long>(degree[n-i]);
        }
        return max_importance;
    }
};