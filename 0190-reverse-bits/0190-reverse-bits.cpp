class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t result = 0;
        uint32_t rightest_bit;

        for (auto i = 0; i < 32; i++){
            rightest_bit = 1 & n;
            result = result << 1;
            result += rightest_bit;
            n = n >> 1;
        }

        return result;
    }
};