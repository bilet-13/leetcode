class Solution {
public:
    vector<string> findItinerary(vector<vector<string>>& tickets) {
        // travsal problem:     use all edge to construct the smallast lexical parh
        // dfs
        unordered_map<string, priority_queue<string, vector<string>, greater<string>>> graph;
        stack<string> s;
        vector<string> itinerary;

        for (const auto& ticket : tickets) {
            graph[ticket[0]].push(ticket[1]);
        }
        s.push("JFK");

        while (!s.empty()) {
            auto city = s.top();
            auto& pq = graph[city];

            if (!pq.empty()) {
                auto toCity = pq.top();
                pq.pop();
                s.push(toCity);
            } else {
                itinerary.push_back(city);
                s.pop();
            }
        }

        reverse(itinerary.begin(), itinerary.end());
        return itinerary;
    }
};
