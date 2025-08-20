class Solution {
public:
    int jump(vector<int>& nums) {
            
        int curFarthest = nums[0];
        int curEnd = 0;
        int result = 0;

        for (int i = 0; i < nums.size() - 1; ++i) {
            curFarthest = max(curFarthest, i + nums[i]);
            if (i == curEnd) {
                curEnd = curFarthest;
                result++;

                if (curEnd >= nums.size() - 1) {
                    break;
                }
            }
        }
        return result;
    }
};