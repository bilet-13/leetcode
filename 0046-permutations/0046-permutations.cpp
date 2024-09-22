class Solution {

private:

    void getPermute(vector<vector<int>>& result, vector<int>& nums, int start, vector<int>& current){
        if(current.size() == nums.size()){
            result.push_back(current);
            return;
        }

        for(int i = start; i < nums.size(); i++){
            swap(nums[start], nums[i]);

            for(int j = start; j < nums.size(); j++){
                current.push_back(nums[j]);
                getPermute(result, nums, j+1, current);
                current.pop_back();
            }

            swap(nums[start], nums[i]);
        }
        return;
    }
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> current;

        getPermute(result, nums, 0, current);
        return result;
    }
};