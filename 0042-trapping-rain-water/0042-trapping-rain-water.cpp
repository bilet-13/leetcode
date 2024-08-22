class Solution {
public:
    int trap(vector<int>& height) {
        auto left = 0;
        auto right = height.size() - 1;
        auto water = 0;
        auto left_max = height[left];
        auto right_max = height[right];

        while (right > left){

            if(left_max < right_max){
                left += 1;
                left_max = max(height[left], left_max);
                water += max(left_max-height[left], 0);
            
            }
            else{
                right -= 1;
                right_max = max(height[right], right_max);
                water += max(right_max-height[right], 0);
                
            }

        }

        return water;
    }
};