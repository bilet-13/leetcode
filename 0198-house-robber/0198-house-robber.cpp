class Solution {
public:
    int rob(vector<int>& nums) {
        vector<int> max_rob(nums.size()+1, 0);
        max_rob[0] = 0;
        max_rob[1] = nums[0];

        for (auto i = 2; i <= nums.size(); i++){
            max_rob[i] = max(max_rob[i-1], max_rob[i-2] + nums[i-1]); 
        }

        return max_rob[nums.size()];
    }
};