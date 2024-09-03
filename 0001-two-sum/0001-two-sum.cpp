class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> num_index;

        for(auto i = 0; i < nums.size(); i++){
            auto iter = num_index.find(target-nums[i]);

            if (iter != num_index.end()){
                vector<int> answer = {iter->second, i};
                return answer;
            }

            num_index[nums[i]] = i;
        }

        vector<int> non_found_answer;
        return non_found_answer;
    }
};