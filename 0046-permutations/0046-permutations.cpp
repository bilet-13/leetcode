class Solution {

private:

    void getPermute(vector<vector<int>>& result, vector<int>& nums, int start){
        if(start == nums.size()-1){
            result.push_back(nums);
            return;
        }

        for(int i = start; i < nums.size(); i++){
            swap(nums[start], nums[i]);
            
            getPermute(result, nums, start+1);
            
            swap(nums[start], nums[i]);
        }
        return;
    }
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> result;

        getPermute(result, nums, 0);
        return result;
    }
};