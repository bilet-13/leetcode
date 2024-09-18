class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> longest_subsequence(nums.size()+1, 0);
        int max_len = 0;
        longest_subsequence[0] = 0;

        for(int i = 1; i <= nums.size(); i++){
            int max_cur_num = longest_subsequence[0];
            int index = i - 1;

            for(int j = 0; j < index; j++){
                if(nums[j] < nums[index]){
                    max_cur_num = max(max_cur_num, longest_subsequence[j+1]);
                }
            }
            longest_subsequence[i] = max_cur_num+1;
            max_len = max(max_len, longest_subsequence[i]);
        }
        return  max_len;
    }
};