class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        vector<int> dist(n, INT_MAX);
        dist[src] = 0;

        for (int i = 0; i < k + 1; ++i) {
            vector<int> update_dist(n, INT_MAX);

            for (const auto& flight : flights) {
                if ((dist[flight[1]] - dist[flight[0]]) > flight[2]) {
                    update_dist[flight[1]] = min(update_dist[flight[1]], dist[flight[0]] + flight[2]);
                } 
            }

            for (int j = 0; j < n; ++j) {
                if (update_dist[j] != INT_MAX) {
                    dist[j] = update_dist[j];
                }
            }
        }
        return dist[dst] == INT_MAX ? -1 : dist[dst];
    }
};