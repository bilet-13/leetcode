class Solution {
public:
    int maxProduct(vector<int>& nums) {
        vector<int> maxSoFar(nums.size()); // maxSoFar[i]: the max product include nums[i]
        vector<int> minSoFar(nums.size());

        maxSoFar[0] = nums[0];
        minSoFar[0] = nums[0];

        for (int i = 1; i < nums.size(); ++i) {
            vector<int> candidates = {nums[i], nums[i] * maxSoFar[i - 1], nums[i] * minSoFar[i - 1]};
            maxSoFar[i] = *max_element(candidates.begin(), candidates.end());
            minSoFar[i] = *min_element(candidates.begin(), candidates.end());
        }

        return *max_element(maxSoFar.begin(), maxSoFar.end());
    }
};
