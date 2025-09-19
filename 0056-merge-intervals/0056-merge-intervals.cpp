class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), 
            [](const vector<int>& a, const vector<int>& b){
                if (a[0] != b[0]) {
                    return a[0] < b[0];
                } 
                return a[1] < b[1];
        });

        vector<vector<int>> merged;

        merged.push_back(intervals[0]);
        for (int i = 1; i < intervals.size(); ++i) {
            auto& last = merged.back();
            if (last[1] < intervals[i][0]) {
                merged.push_back(intervals[i]); // not merge
            } else {
                last[1] = max(last[1], intervals[i][1]);
            }
        }
        return merged;
    }
};
