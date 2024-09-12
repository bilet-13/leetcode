class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int w_size = 0;
        int sum = 0;
        int min_len = INT_MAX;

        for (int i = 0; i < nums.size(); i++){
            if (i > 0){
                sum -= nums[i-1];
                w_size--;
            }

            while(sum < target && i+w_size < nums.size()){
                w_size++;
                sum += nums[i+w_size-1];
            }
            if(sum >= target){
                min_len = min(min_len, w_size);
            }
        }
        return min_len == INT_MAX ? 0 : min_len ;
    }
};