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
            int last = merged.size() - 1;
            if (merged[last][1] < intervals[i][0]) {
                merged.push_back(intervals[i]); // not merge
            } else {
                merged[last][1] = max(merged[last][1], intervals[i][1]);
            }
        }
        return merged;
    }
};
