class Solution {
private:
    void findPermute(vector<int> &nums, int start, vector<int> &current, vector<vector<int>> &result) {
        if (current.size() == nums.size()) {
            result.push_back(current);
            return;
        }

        for(int i = start; i < nums.size(); ++i) {
            swap(nums[i], nums[start]);
            current.push_back(nums[start]);

            findPermute(nums, start + 1, current, result);

            current.pop_back();
            swap(nums[i], nums[start]);
        }
    }

public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> current;

        findPermute(nums, 0, current, result);

        return result;
    }
};
