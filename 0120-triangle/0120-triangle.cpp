class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        vector<vector<int>> min_path;
        min_path.push_back(triangle[0]);

        for(int i = 1; i < triangle.size(); i++ ){
            vector<int> path;
            
            for(int j = 0; j < triangle[i].size(); j++){
                int min_path_parent = INT_MAX;

                if(j-1 >= 0){
                    min_path_parent = min(min_path_parent, min_path[i-1][j-1]);
                }
                if(j < min_path[i-1].size()){
                    min_path_parent = min(min_path_parent, min_path[i-1][j]);
                }
                path.push_back(min_path_parent+triangle[i][j]);
            }
            min_path.push_back(std::move(path));
        }
        return *min_element(min_path[min_path.size()-1].begin(), min_path[min_path.size()-1].end());
    }
};