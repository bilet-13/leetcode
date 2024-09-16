class Solution {
    int getDiffNumber(const string a, const string b){
        int result = 0;
        for(int i = 0; i < a.size(); i++){
            if(a[i] != b[i]) result++;
        }
        return result;
    }
public:
    int minMutation(string startGene, string endGene, vector<string>& bank) {
        if(startGene == endGene){
            return 0;
        }

        unordered_map<string, vector<string>> adjency_list;
        for(const string gene : bank){
            if(getDiffNumber(gene, startGene) == 1){
                adjency_list[startGene].push_back(gene);
            }
            for(const string next_gene : bank){
                if(getDiffNumber(gene, next_gene) == 1){
                    adjency_list[gene].push_back(next_gene);
                }
            }
        }
        
        int min_mutation = -1;
        queue<pair<string, int>> nodes;
        set<string> visited;

        nodes.push({startGene, 0});
        visited.insert(startGene);

        while(!nodes.empty()){
            auto node = nodes.front();
            nodes.pop();

            if(node.first == endGene){
                return node.second;
            }

            for(auto neighbor : adjency_list[node.first] ){
                if(visited.count(neighbor) == 0){
                    nodes.push({neighbor, node.second+1});
                    visited.insert(neighbor);
                }
            }
        }
        return min_mutation;
    }
};