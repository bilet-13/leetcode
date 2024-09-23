class Solution {
public:
    int trailingZeroes(int n) {
        int num_five = 0;
        while(n > 0){
            n /= 5;
            num_five += n;
        }
        
        return num_five;
    }
};