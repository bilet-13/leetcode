class Solution {

private:

    void getPermute(vector<vector<int>>& result, vector<int>& nums, int start) {
        if (start == nums.size() - 1) {
            result.push_back(nums);
            return;
        }

        unordered_set<int> used;  // To track numbers that have been used at the current level

        for (int i = start; i < nums.size(); i++) {
            if (used.count(nums[i])) {
                continue;  // Skip if the number has already been used in this position
            }

            used.insert(nums[i]);  // Mark the number as used

            swap(nums[start], nums[i]);
            
            getPermute(result, nums, start + 1);
            
            swap(nums[start], nums[i]);  // Backtrack
        }
        return;
    }

public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<vector<int>> result;

        sort(nums.begin(), nums.end());  // Sort to handle duplicates

        getPermute(result, nums, 0);
        return result;
    }
};
