class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> longest_subsequence(nums.size(), 1);
        int max_len = 1;

        for(int i = 1; i < nums.size(); i++){
            int max_cur_num = 0;

            for(int j = 0; j < i; j++){
                if(nums[j] < nums[i]){
                    max_cur_num = max(max_cur_num, longest_subsequence[j]);
                }
            }
            longest_subsequence[i] = max_cur_num+1;
            max_len = max(max_len, longest_subsequence[i]);
        }
        return  max_len;
    }
};