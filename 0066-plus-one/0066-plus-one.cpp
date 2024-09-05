class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int carry = 0;
        digits[digits.size()-1] += 1;
        vector<int> answer;

        for (int i = digits.size()-1; i >= 0; i--){
            int num = digits[i] + carry;
            carry = num / 10;
            digits[i] = num % 10;
        }

        if (carry != 0){
            answer.push_back(carry);
        }

        for(int num : digits){
            answer.push_back(num);
        }
        return answer;
    }
};