class Solution {
public:
    bool isHappy(int n) {
        // two pointer
        // slow , fast pointer
        // slow do 1 step each time and fast do 2 steps each time
        // if slow == fast cycle
        // else if slow or fast == 1 return true
        auto getSquareSum = [](int n) -> int {
            int result = 0;
            while (n > 0) {
                int digit = n % 10;
                n = n / 10;
                result += pow(digit, 2);
            }
            return result;
        };

        int slow = n;
        int fast = n;

        while (slow != 1 && fast != 1) {
            slow = getSquareSum(slow);
            fast = getSquareSum(getSquareSum(fast));

            if (slow != 1 && slow == fast) {
                return false;
            }
        }

        return true;
    }
};
