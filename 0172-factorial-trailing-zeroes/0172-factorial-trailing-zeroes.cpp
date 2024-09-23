class Solution {
public:
    int trailingZeroes(int n) {
        int num_five = 0;
        int num_two = 0;

        for(int i = 1; i<= n; i++){
            auto num = i;

            while(num % 5 == 0 && num != 0){
                num_five++;
                num /= 5;
            }

            num = i;

            while(num % 2 == 0 && num != 0){
                num_two++;
                num /= 2;
            }
        }
        return min(num_five, num_two);
    }
};