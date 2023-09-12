class Solution {
public:
    bool isValid(string s) {
        
        map<char, char>parenthess_map{
            {'(',')'}, {'{','}'},  {'[',']'}
        };

        stack<char> char_stack;
        char tmp_char,cmp_char;
        

        for (size_t i = 0; i < s.size(); i++)
        {
            tmp_char = s[i];
            
            if(tmp_char == '('|| tmp_char == '{' || tmp_char == '[')
                char_stack.push(tmp_char);
            else{
                if(char_stack.empty())
                    return false;
                cmp_char = char_stack.top();
                char_stack.pop();
                if(parenthess_map[cmp_char] != tmp_char)
                    return false;
            }
        }
        
        if( char_stack.empty())
            return true;
        else
            return false;
         
    }
};