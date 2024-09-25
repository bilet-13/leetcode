class Solution {

    void findCombination(vector<int>& candidates, int& index, int target, vector<vector<int>>& result, vector<int>& current, int sum){
        if(sum > target){
            return;
        }

        else if( sum == target){
            result.push_back(current);
            return;
        }

        for(int i = index; i < candidates.size(); i++){
            current.push_back(candidates[i]);
            findCombination(candidates, i, target, result, current, sum+candidates[i]);
            current.pop_back();
        }
        return;
    }   

public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> result;
        vector<int> current;

        sort(candidates.begin(), candidates.end());
        
        int index = 0;
        findCombination(candidates, index , target, result, current, 0);

        return result;
    }
};