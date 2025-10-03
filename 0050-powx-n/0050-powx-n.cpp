class Solution {
public:
    double myPow(double x, int n) {
       long long int k = n;
       if (k < 0) {
        k = -k;
       }
       double result = pow(x, k);

       return n >= 0 ? result : 1 / result;
    }

    double pow(double x, long long int n) {
        if (n == 0) {
        return 1;
       } else if (n == 1) {
        return x;
       } else if (n % 2 == 0) {
        double result = pow(x, n / 2);
        return result * result;
       } else {
        double result = pow(x, (n - 1) / 2); 
        return x * result * result;
       }
    }
};
