class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        vector<int> plusOneResult;

        int carry = 1;

        // 1 start from rightmost digit and add 1 and maintain carry
        // 2 for each digit add carry and store the result
        for (int i = digits.size() - 1; i >= 0; --i) {
            int sum = carry + digits[i];
            int digit = sum % 10;
            carry = sum / 10;

            plusOneResult.push_back(digit);            
        }
        if (carry > 0) {
            plusOneResult.push_back(carry); 
        }

        // 3 reverse the result to maintain the order
        reverse(plusOneResult.begin(), plusOneResult.end());

        return plusOneResult;
    }
};
