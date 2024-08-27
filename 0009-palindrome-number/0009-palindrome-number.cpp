class Solution {
public:
    bool isPalindrome(int x) {
        
        if (x < 0){
            return false;
        }

        string x_str = to_string(x);
        int left = 0;
        int right = x_str.size() - 1;

        while (left < right){
            if (x_str[left] != x_str[right]){
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
};