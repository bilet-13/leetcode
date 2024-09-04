class Solution {
public:
    int snakesAndLadders(vector<vector<int>>& board) {
        int n = board.size();
        queue<pair<int, int>> nodes;
        nodes.push(make_pair(0, 1));
        
        vector<int> visited(n*n+1, 0);
        visited[1] = 1;

        int min_step = -1;

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
                auto next_pos = getPos(next, n);
                auto next_label = next;
                if (board[next_pos.first][next_pos.second] != -1){
                    next_label = board[next_pos.first][next_pos.second];
                }

                if (!visited[next_label]){
                    visited[next_label] = 1;
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