class Solution {
public:
    int maxSubarraySumCircular(vector<int>& nums) {
        
        int sum = 0;
        int max_sum = INT_MIN;
        int cur_max = INT_MIN;
        int cur_min = 0;

        for(const auto& num : nums){
            sum += num;
        }

        for(const auto& num : nums){
            cur_max = max(0, cur_max);
            cur_max += num;
            max_sum = max(max_sum, cur_max);

            cur_min = min(0, cur_min);
            cur_min += num;
            max_sum = cur_min != sum ? max(max_sum, sum-cur_min) : max_sum;
        }
        return max_sum;
    }
};