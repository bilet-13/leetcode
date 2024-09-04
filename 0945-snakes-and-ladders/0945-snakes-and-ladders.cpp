class Solution {
public:
    int snakesAndLadders(vector<vector<int>>& board) {
        int n = board.size();
        queue<pair<int, int>> nodes;
        nodes.push(make_pair(0, 1));
        
        set<int> visited;
        visited.insert(1);

        int min_step = -1;

        unordered_map<int, pair<int,int>> label_pos;
    
        for(int i = 1; i <= n*n; i++){
            auto pos = getPos(i, n);
            label_pos[i] = pos;
            cout<<pos.first<<" "<<pos.second<<endl;
        }

        while(!nodes.empty()){
            auto step_node = nodes.front();
            nodes.pop();

            int step = step_node.first;
            auto label = step_node.second;

            if(label == n*n ){
                min_step = step;
                return min_step;
            }

            for (int next = label+1 ; next <= min(label+6, n*n); next++){
                auto next_pos = label_pos[next];
                auto next_label = next;
                if (board[next_pos.first][next_pos.second] != -1){
                    next_label = board[next_pos.first][next_pos.second];
                }

                if (!visited.count(next_label)){
                    visited.insert(next_label);
                    nodes.push(make_pair(step+1, next_label));
                }
            }  
        }
        return min_step;
    }

    pair<int, int> getPos(int label, int n){
        label -= 1;
        int row =  n - 1 - label/n;

        int column;

        if( row % 2 == (n-1) % 2){
            column = label % n ;
        }
        else{
            column = n - 1 - label % n ;
        }

        return make_pair(row, column);
    }
};