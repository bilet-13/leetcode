class Solution {
public:
    double myPow(double x, int n) {
        if(x == 0.0 || n == 1){
            return x;
        }
        if(n == 0){
            return 1;
        }

        long long int power = n;
        if(power < 0){
            x = 1 / x;
            power = -power; 
        }

        double odd_x = 1;

        if(power%2 == 1){
            power -= 1;
            odd_x = x;
        }

        return odd_x * myPow(x*x, power/2);
    }
};