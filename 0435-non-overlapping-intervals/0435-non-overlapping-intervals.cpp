class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
       sort(intervals.begin(), intervals.end(), [](const vector<int> a, const vector<int> b) {
        if (a[1] != b[1]) {
            return a[1] < b[1];
        } 
        return a[0] < b[0];
       });

       int prevEnd = INT_MIN;
       int nonOverlapIntervalNum = 0;

       for (auto iv : intervals) {
        if (prevEnd <= iv[0]) {
            nonOverlapIntervalNum++;
            prevEnd = iv[1];
        }
       }

       return intervals.size() - nonOverlapIntervalNum;
    }
};
