class Solution {
public:
    int rob(vector<int>& nums) {
        // 2 ^n exclude the adjacent neigobor combination
        int n = nums.size();
        if (n <= 3) {
            return *max_element(nums.begin(), nums.end());
        }

        vector<int> robExcludeLast(n - 1);
        robExcludeLast[0] = nums[0];
        robExcludeLast[1] = max(nums[1], robExcludeLast[0]);

        vector<int> robExcludeFirst(n, 0);
        robExcludeFirst[1] = nums[1];
        robExcludeFirst[2] = max(nums[2], robExcludeFirst[1]);

        for (int i = 2; i < n - 1; ++i) {
            robExcludeLast[i] = max(robExcludeLast[i - 1], nums[i] + robExcludeLast[i - 2]);
        }

        for (int i = 3; i < n; ++i) {
            robExcludeFirst[i] = max(robExcludeFirst[i - 1], nums[i] + robExcludeFirst[i - 2]);
        }

        return max(robExcludeLast[n - 2], robExcludeFirst[n - 1]);
    }
};
