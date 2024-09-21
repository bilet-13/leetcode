class Solution {
public:
    int maxSubarraySumCircular(vector<int>& nums) {
        
        int total_sum = 0;
        int max_sum = INT_MIN;
        int min_sum = INT_MAX;
        int cur_max = 0;
        int cur_min = 0;

        for(const auto& num : nums){
            total_sum += num;
        }

        for(const auto& num : nums){
            cur_max = max(0, cur_max);
            cur_max += num;
            max_sum = max(max_sum, cur_max);

            cur_min = min(0, cur_min);
            cur_min += num;
            min_sum = min(min_sum, cur_min);
        }

        return min_sum == total_sum ? max_sum : max(max_sum, total_sum-min_sum);
    }
};