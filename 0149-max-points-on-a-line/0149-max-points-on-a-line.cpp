class Solution {
private:
    double getSlope(vector<int> point1, vector<int> point2){
        auto dy = (double(point2[1]) - double(point1[1]));
        auto dx = (double(point2[0]) - double(point1[0]));
        return dy / dx;
    }
public:
    int maxPoints(vector<vector<int>>& points) {
        int max_points = 1;

        for(int i = 0; i < points.size(); i++){
            unordered_map<double, int> slopes;
            int vertical = 1;

            for(int j = i+1; j < points.size(); j++){
                if(points[i][0] != points[j][0]){
                    double slope = getSlope(points[i], points[j]);

                    if(slopes.find(slope) == slopes.end()){
                        slopes[slope] = 1;
                    }

                    slopes[slope] += 1;
                    max_points = max(max_points, slopes[slope]);
                }
                else{
                    vertical += 1;
                    max_points = max(max_points, vertical);
                }
                
            }
        }
        return max_points;
    }
};