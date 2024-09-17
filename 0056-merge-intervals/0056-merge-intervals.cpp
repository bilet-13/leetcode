class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        
        sort(intervals.begin(), intervals.end());
        
        vector<vector<int>> non_overlapping_intervals;
        vector<int> prev_interval = {intervals[0][0], intervals[0][1]};

        for(int i = 1; i < intervals.size(); i++){
             if(intervals[i][0] > prev_interval[1]){
                non_overlapping_intervals.push_back(prev_interval);
                prev_interval = {intervals[i][0], intervals[i][1]};
             }
             else{
                prev_interval[1] = max(prev_interval[1], intervals[i][1]);
             }
        }
        non_overlapping_intervals.push_back(prev_interval);
        
        return non_overlapping_intervals;
    }
};