class Solution {
public:
    bool canJump(vector<int>& nums) {
        // from i jump to j that j <= i + length and j + nums[j] is maximum
        // greedy; time complexity O(n^2) /
        int idx = 0;

        while (idx < nums.size()) {
            int length = nums[idx];
            int nextIdx = idx;

            for (int j = idx + 1; j <= idx + length && j < nums.size(); ++j) {
                if (nums[nextIdx] + nextIdx < nums[j] + j) {
                    nextIdx = j;
                } 
            }

            if (nextIdx + nums[nextIdx] >= nums.size() - 1) {
                return true;
            } else if (nextIdx == idx) {
                return false; 
            }

            idx = nextIdx;
        }
        return true;
    }
};
