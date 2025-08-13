class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> appearNums;

        for (const auto& num : nums) {
            if (appearNums.count(num)) {
                return true;
            }
            appearNums.insert(num);
        }

        return false;
    }
};