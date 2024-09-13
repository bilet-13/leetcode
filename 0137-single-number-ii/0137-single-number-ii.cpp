class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int ones = 0;
        int twos = 0;

        for(int num : nums){
            twos |= (ones & num);
            ones ^= num;

            int mask = ~(ones & twos);
            ones &= mask;
            twos &= mask;
        }
        return ones;
    }
};