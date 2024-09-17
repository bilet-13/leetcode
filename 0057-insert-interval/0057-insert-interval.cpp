class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        int pos = findInsertPos(intervals, newInterval);
        intervals.insert(intervals.begin()+pos, newInterval);
        cout<<pos<<endl;
        mergeIntervals(intervals, pos);
        return intervals;
    }

    int findInsertPos(vector<vector<int>>& intervals, vector<int>& newInterval){
        int left = 0;
        int right = intervals.size() - 1;

        while(left <= right){
            int mid = left + (right-left) / 2;

            if(intervals[mid][0] == newInterval[0]){
                return mid;
            }
            else if(intervals[mid][0] > newInterval[0]){
                right = mid - 1;
            }
            else{
                left = mid + 1;
            }
        }
        return left;
    }

    void mergeIntervals(vector<vector<int>>& intervals, int pos){
        int left = pos;
        int right = pos;

        int start = intervals[pos][0];
        int end = intervals[pos][1];

        while(left-1 >= 0 && intervals[left-1][1] >= start){
            left--;
            start = min(intervals[left][0], start);
            end = max(intervals[left][1], end);
        }

        while(right+1 < intervals.size() && intervals[right+1][0] <= end){
            right++;
            end = max(intervals[right][1], end);
        }
        cout<<left<< " "<< right<<endl;
        auto iter = intervals.erase(intervals.begin()+left, intervals.begin()+right+1);
        intervals.insert(iter, {start, end});
    }
};