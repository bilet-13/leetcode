class Solution {
private:
    void getCombine(vector<vector<int>>& result, int start, int n, int k, vector<int>& current){
        if(current.size() == k){
            result.push_back(current);
            return;
        }

        for(int i = start; i <= n; i++){
            current.push_back(i);
            getCombine(result, i+1, n, k, current);
            current.pop_back();
        }
        return;
    }
public:
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> result;
        vector<int> current;
        getCombine(result, 1, n, k, current);

        return result;
    }
};