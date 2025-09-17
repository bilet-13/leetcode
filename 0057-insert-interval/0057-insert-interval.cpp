class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        // step 1: insert new interval to interval and keep ascending
        // time complexity O(n + 1) n: size of intervals
        vector<vector<int>> allIntervals;
        vector<vector<int>> mergedIntervals;
        bool isNewIntervalInAllIntervals = false;

        for (int i = 0; i < intervals.size(); ++i) {
            if (intervals[i][0] >= newInterval[0]) {
                allIntervals.push_back(newInterval);
                isNewIntervalInAllIntervals = true;
            }
            allIntervals.push_back(intervals[i]);
        }

        if (!isNewIntervalInAllIntervals) {
            allIntervals.push_back(newInterval);
        }
        mergedIntervals.push_back(allIntervals[0]);
        
        // step 2: turn the intervals to non overlaping by merging
        // time complexity O(n + 1) n + 1(new interval) n: size of intervals
        for (int i = 0; i < allIntervals.size(); ++i) {
            int last = mergedIntervals.size() - 1; 
            if (mergedIntervals[last][1] < allIntervals[i][0]) {
                mergedIntervals.push_back(allIntervals[i]);
                continue;
            }

            mergedIntervals[last][1] = max(mergedIntervals[last][1], allIntervals[i][1]);
        }
       
        return mergedIntervals;// time complexity O(n + 1) = O(n) n: size of the vector intervals
    }
};
