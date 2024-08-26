class Solution {
public:
    int hammingWeight(int n) {
        int hamming_weight = 0;

        while(n != 0){
            hamming_weight += n&1;
            n = n >> 1;
        }

        return hamming_weight;
    }
};