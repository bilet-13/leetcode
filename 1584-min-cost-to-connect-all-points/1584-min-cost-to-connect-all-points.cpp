class Solution {
public:
    int minCostConnectPoints(vector<vector<int>>& points) {
        int n = points.size();
        int minCost = 0;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        vector<bool> inMST(n, false);
        vector<int> minDist(n, INT_MAX);
        minDist[0] = 0;

        pq.emplace(0, 0);

        while (!pq.empty()) {
            auto [cost, u] = pq.top();
            pq.pop();

            if (inMST[u]) {
                continue;
            }
            inMST[u] = true;
            minCost += cost;

            for (int v = 0; v < n; ++v) {
                if (!inMST[v]) {
                    int dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1]);
                    if (dist < minDist[v]) {
                        minDist[v] = dist;
                        pq.emplace(dist, v);
                    }
                }
            }
        }
        return minCost;
    }
};
