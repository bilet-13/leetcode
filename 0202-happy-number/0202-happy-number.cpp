class Solution {
    int getSquareSum(int n){
        auto sum = 0;
        int digit;

        while (n) {
            digit = n % 10;
            n /= 10;
            sum += pow(digit, 2);
        }
        return sum;
    }

public:
    bool isHappy(int n) {
        auto slow = n;
        auto fast = n;

        while(true){
            slow = getSquareSum(slow);
            fast = getSquareSum(fast);
            fast = getSquareSum(fast);

            if (fast == 1){
                return true;
            }

            if(fast == slow){
                return false;
            }
        }

    }
};