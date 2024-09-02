class Solution {
public:
    bool isHappy(int n) {
        int digit;
        int sum = 0;
        set<int> numbers;

        while(true){
            sum = 0;

            while(n != 0){
                digit = n % 10;
                n /= 10;
                sum += pow(digit, 2);
            }
            n = sum;

            if (sum == 1){
                return true;
            }

            if(numbers.count(sum)){
                return false;
            }

            numbers.insert(sum);
        }

    }
};