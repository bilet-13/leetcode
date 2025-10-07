class Solution {
public:
    int minimumTime(int n, vector<vector<int>>& relations, vector<int>& time) {
        vector<vector<int>> graph(n + 1);
        vector<int> inDegrees(n + 1, 0);
        vector<int> minStartTime(n + 1);
        queue<int> q;
        int minTime = 0;

        for (auto& r : relations) {
            graph[r[0]].push_back(r[1]);
            inDegrees[r[1]] += 1;
        }

        for (int i = 1; i <= n; ++i) {
            if (inDegrees[i] == 0) {
                q.push(i);
            }
        }

        while (!q.empty()) {
            auto label = q.front();
            q.pop();

            int end = minStartTime[label] + time[label - 1];
            minTime = max(minTime, end);

            for (auto& next: graph[label]) {
                minStartTime[next] = max(minStartTime[next], end);
                inDegrees[next]--;

                if (inDegrees[next] == 0) {
                    q.push(next);
                }
            }

        }
        return minTime;
    }
};