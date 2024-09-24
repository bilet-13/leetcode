class Solution {
public:
    int minCost(string colors, vector<int>& neededTime) {
        
        int total_time = 0;
        int left = 0;
        int sum = 0;
        int max_time = 0;

        for(int right = 0; right < neededTime.size(); right++){
            char color = colors[right];

            while(left < right && colors[left] != color){
                left++;
            }

            if(right == neededTime.size()-1 || colors[right+1] != color){
                if(left < right){
                    int max_time = neededTime[left];

                    total_time += neededTime[left];
                    while( left+1 <= right){
                        left++;
                        total_time += neededTime[left];
                        max_time = max(max_time, neededTime[left]);
                    }
                    total_time -= max_time;
                }
            }
        }
        return total_time;
    }
};