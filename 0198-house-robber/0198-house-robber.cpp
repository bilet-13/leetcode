class Solution {
public:
    int rob(vector<int>& nums) {
        // 1, 1, 3, 4
        // brute force 2^n
        int n = nums.size();
        if (n <= 2) {
            return *max_element(nums.begin(), nums.end());
        }

        vector<int> rob(n);
        rob[0] = nums[0];
        rob[1] = max(nums[0], nums[1]);

        for (int i = 2; i < n; ++i) {
            rob[i] = max(rob[i - 1], rob[i - 2] + nums[i]);
        }

        return rob[n - 1];
    }
};
