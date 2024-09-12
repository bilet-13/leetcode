class Solution {
public:
    vector<int> findSubstring(string s, vector<string>& words) {
        unordered_map<string, int> word_count;
        int w_size = 0;
        int left = 0;
        int w_len = words[0].size();
        vector<int> result;

        for (string word : words){
            if(word_count.find(word) == word_count.end()){
                word_count[word] = 0;
            }
            word_count[word] += 1;
        }

        for(int i = 0; i < w_len; i++){
            unordered_map<string, int> current_count = word_count;
            int count = 0;
            for (int j = i; j + w_len <= s.size(); j += w_len){
                auto iter = current_count.find(s.substr(j, w_len));

                if(iter != current_count.end()){
                    if(iter->second > 0){
                        count++;
                    }
                    iter->second--;
                }

                int pop_start = j - (words.size()*w_len);
                if (pop_start >= 0 && pop_start+w_len <= s.size()){
                    int pop_start = j - (words.size()*w_len);
                    auto pop_iter = current_count.find(s.substr(pop_start, w_len));

                    if(pop_iter != current_count.end()){
                        pop_iter->second++;

                        if(pop_iter->second > 0)count--;
                    }
                }

                if(count == words.size()){
                    result.push_back(j - (words.size()-1)*w_len);
                }
            }
        }
        return result;
    }
};