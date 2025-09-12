class Solution {
public:
    bool mergeTriplets(vector<vector<int>>& triplets, vector<int>& target) {
        vector<int> cur = {0, 0, 0};
        int triplet_length = 3;
        // init a vec cur = {0, 0, 0}
        // i is 0, 1, 2
        auto isAnyExceedTarget = [&](vector<int> t) -> bool {
            for (int i = 0; i < triplet_length; ++i) {
                if (t[i] > target[i]) {
                    return true;
                }
            }
            return false;
        };
         
        for (const auto& t : triplets) {
            if (isAnyExceedTarget(t)) {
                continue;
            }

            for (int i = 0; i < triplet_length; ++i) {
                cur[i] = max(t[i], cur[i]);
            }
        }

        // for loop triplets for each triplet t 
        // if any t[i] exceed target[i]
        // skip t else if the cur[i] != target[i] update cur[i] 
        // else continue
        // in the end check the cur == target or not
        return cur == target;
    }
};
