class Solution {
public:
    int majorityElement(vector<int>& nums) {
        pair<int, int> max_element;
        map<int,int> my_map;
        map<int,int>::iterator itr;

        max_element.second = 0;

        for (size_t i = 0; i < nums.size(); i++)
        {
            itr = my_map.find(nums[i]);
            if(itr != my_map.end()){
                itr->second++;
            }
            else{
                my_map[nums[i]] = 1;
            }
            
            if(my_map[nums[i]] > max_element.second)
            {
                max_element.second = my_map[nums[i]];
                max_element.first = nums[i];
            }
        }

        return max_element.first;
        
    }
};