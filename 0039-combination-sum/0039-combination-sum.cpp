class Solution {

    void findCombination(vector<int>& candidates, int target, set<multiset<int>>& result, multiset<int>& current, int sum){
        if(sum > target){
            return;
        }

        else if( sum == target){
            if(result.count(current) == 0){
                result.insert(current);
            }
            return;
        }

        for(auto& num : candidates){
            current.insert(num);
            findCombination(candidates, target, result, current, sum+num);
            current.erase(current.find(num));
        }
        return;
    }   

public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        set<multiset<int>> result;
        multiset<int> current;
        vector<vector<int>> return_vec;

        findCombination(candidates, target, result, current, 0);

        for(auto& combination : result){
            vector<int> tmp(combination.begin(), combination.end());
            return_vec.push_back(std::move(tmp));
        }

        return return_vec;
    }
};