class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        
        map<int, int> my_map;
        map<int, int>::iterator iter;

        for(int i = 0; i< nums.size() ; i++){

            iter = my_map.find(nums[i]);

            if(iter != my_map.end()){
                if( abs(iter->second - i) <= k)
                    return true;

                iter->second = i;
            }
            else{
                my_map[nums[i]] = i;
            }
        }
        return false;

    }
};