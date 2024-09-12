class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int single = 0;

        for(int num : nums){
            single = single ^ num;
        }
        return single;
    }
};