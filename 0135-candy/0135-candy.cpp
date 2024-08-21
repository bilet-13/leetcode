class Solution {
public:
    int candy(vector<int>& ratings) {
        if(ratings.size() == 1){
            return 1;
        }

        vector<int> candies;
        for (auto i = 0; i<ratings.size(); i++){
            candies.push_back(1);
        }

        for (auto i = 1; i < ratings.size(); i++){
            if (ratings[i-1] > ratings[i]){
                if (candies[i] == candies[i-1]){
                    candies[i-1] += 1;
                    auto current_n = i - 1 ;
                    auto left_n = i - 2;
                    while(left_n >= 0 and ratings[left_n] > ratings[current_n] and candies[left_n] <= candies[current_n]){
                        candies[left_n] += 1;
                        left_n -= 1;
                        current_n -= 1;

                    }
                }
                continue;
            }
            else if (ratings[i-1] < ratings[i]) {
                candies[i] = candies[i-1] + 1;
            }
        }

        int minimum_candies = 0;
        for (auto num_candy : candies){
            minimum_candies += num_candy;
        }
        return minimum_candies;
    }
};