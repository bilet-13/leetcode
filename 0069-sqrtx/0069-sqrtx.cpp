class Solution {
public:
    int mySqrt(int x) {
        long long int i = 0;

        while(i*i < x){
            i++;
        }
        return i*i == x ? i : i-1;
    }
};