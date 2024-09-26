class Solution {
public:
    int calculate(string s) {
        stack<int> nums;

        int num = 0;
        char sign = '+';
        s += '+';

        for(const auto& chr : s){

            if(chr >= '0' && chr <= '9'){
                num = num * 10 + (chr - '0');
            }
            else if(chr == ' '){
                continue;
            }

            else if(sign == '+' || sign == '-'){
                num = sign == '+' ?  num : -1 * num;
                nums.push(num);

                sign = chr;
                num = 0;
            }

            else if(sign == '*' || sign == '/'){
                int prev = nums.top();
                nums.pop();

                num = sign == '*' ? prev * num : prev / num;
                nums.push(num);
                
                sign = chr;
                num = 0;
            }
        }

        int sum = 0;

        while(!nums.empty()){
            sum += nums.top();
            nums.pop();
        }
        return sum;
    }
};