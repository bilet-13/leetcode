class Solution {
public:
    vector<int> minInterval(vector<vector<int>>& intervals, vector<int>& queries) {
        unordered_map<int, int> queryResult;
        vector<int> originQueries;
        vector<int> result;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> minHeap;// size, end;
        
        for (auto q : queries) {
            originQueries.push_back(q);
        }

        sort(intervals.begin(), intervals.end());
        sort(queries.begin(), queries.end());

        int intervalIdx = 0; 
        for (auto q : queries) {
            while (intervalIdx < intervals.size() && intervals[intervalIdx][0] <= q) {
                int length = intervals[intervalIdx][1] - intervals[intervalIdx][0] + 1;
                minHeap.emplace(length, intervals[intervalIdx][1]);
                intervalIdx++;
            }

            while (!minHeap.empty() && minHeap.top().second < q) {
                minHeap.pop();
            }
            queryResult[q] = minHeap.empty() ? -1 : minHeap.top().first;
        }

        for (auto q : originQueries) {
            result.push_back(queryResult[q]);
        }

        return result;
    }
};
