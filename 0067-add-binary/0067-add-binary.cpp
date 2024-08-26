class Solution {
public:
    string addBinary(string a, string b) {
        reverse(a.begin(), a.end());
        reverse(b.begin(), b.end());
        string answer = "";
        int carry = 0;
        int index = 0;
        int value = 0;
        
        while (index < a.length() || index < b.length()){
            value = carry;
            if (index < a.length()){
                value += (a[index] - '0');
            }
            if (index < b.length()){
                value += (b[index] - '0');
            }
            answer += char((value % 2) + '0');
            carry = value / 2;

            index++;
        }
        if(carry != 0){
            answer += char(carry + '0');
        } 
        
        reverse(answer.begin(), answer.end());
        return answer;
    }
};