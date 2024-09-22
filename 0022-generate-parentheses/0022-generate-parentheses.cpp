class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> parentheses_result;
        queue<pair<string, int>> parentheses;
        int len = 1;

        parentheses.push({"(", 1});

        while(!parentheses.empty()){
            int size = parentheses.size();

            if(len == 2*n){
                while(!parentheses.empty()){
                    parentheses_result.push_back(parentheses.front().first);
                    parentheses.pop();
                }
                break;
            }

            len += 1;
            for(int i = 0; i < size; i++){
                const auto cur = parentheses.front();
                parentheses.pop();

                int right = cur.first.size() - cur.second;
                if(cur.second > right){
                    parentheses.push({cur.first+")", cur.second});
                }
                if(cur.second < n){
                    parentheses.push({cur.first+"(", cur.second+1});
                }
                
            }
        }
        return parentheses_result;
    }
};