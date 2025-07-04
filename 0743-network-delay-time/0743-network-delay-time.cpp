const int INF = numeric_limits<int>::max();
class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        vector<vector<pair<int, int>>> graph(n + 1);
        vector<int> dist(n + 1, INF);
        dist[k] = 0;

        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        pq.emplace(0, k);

        // build graph
        for (const auto &time : times) {
            graph[time[0]].emplace_back(time[1], time[2]);
        }

        // dijkstra's algo
        while (!pq.empty()) {
            const auto [dis, node] = pq.top();
            pq.pop();

            if (dis > dist[node]) {
                continue;
            }

            for (const auto [neighbor, weight] : graph[node]) {
                if (dist[node] + weight < dist[neighbor]) {
                    dist[neighbor] = dist[node] + weight;
                    pq.emplace(dist[neighbor], neighbor);
                }
            }
        }

        return any_of(dist.begin() + 1, dist.end(), [](const int x) {
            return x == INF;
        }) ? -1 : *max_element(dist.begin() + 1, dist.end());
    }
};
