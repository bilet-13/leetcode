class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_map<int, int>num_length;
        int max_num = 0;
        // 1 3 7 4 2
        for (auto i = 0; i < nums.size(); i++){
            auto iter = num_length.find(nums[i]);
            if (iter != num_length.end()){
                continue;
            }
            
            num_length[nums[i]] = 1;

            auto iter_r = num_length.find(nums[i]+1);
            if(iter_r != num_length.end()){
                num_length[nums[i]] += iter_r->second;
            }

            auto iter_l = num_length.find(nums[i]-1);
            if(iter_l != num_length.end()){
                num_length[nums[i]] += iter_l->second;
            }

            if(iter_r != num_length.end()){
                num_length[nums[i]+iter_r->second] = num_length[nums[i]];
            }
            
             if(iter_l != num_length.end()){
                num_length[nums[i]-iter_l->second] = num_length[nums[i]];
            }

            max_num = max(max_num, num_length[nums[i]]);
        }
        return max_num;
    }
};