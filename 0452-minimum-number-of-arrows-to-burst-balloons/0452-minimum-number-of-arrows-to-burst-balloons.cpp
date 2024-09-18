class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        if(points.size() == 1){
            return points.size();
        }
        
        sort(points.begin(), points.end());

        int prev_start = points[0][0];
        int prev_end = points[0][1];
        int num_non_overlapping_intervals = 0;

        for(int i = 1; i < points.size(); i++){
            if((points[i][0] >= prev_start && points[i][0] <= prev_end ) || (points[i][1] >= prev_start && points[i][1] <= prev_end )){
                prev_start = max(prev_start, points[i][0]);
                prev_end = min(prev_end, points[i][1]);
            }
            else{
                num_non_overlapping_intervals++;
                prev_start =  points[i][0];
                prev_end =  points[i][1];
            }
        }
        num_non_overlapping_intervals++;

        return num_non_overlapping_intervals;
    }
};