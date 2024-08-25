class LRUCache {

private:
    unordered_map<int, pair<int, list<int>::iterator>> cache;
    list<int> lru_list;
    int cache_capacity;

    list<int>::iterator update_lru(int key, list<int>::iterator updated_iter){
        lru_list.erase(updated_iter);
        lru_list.push_front(key);
        return lru_list.begin();
    }

public:
    LRUCache(int capacity) {
        cache_capacity = capacity;
    }
    
    int get(int key) {
        auto iter = cache.find(key);
        if(iter == cache.end()){
            return -1;
        }

        iter->second.second = update_lru(key, iter->second.second);
        return iter->second.first;
    }
    
    void put(int key, int value) {
        auto iter = cache.find(key);

        if(iter != cache.end()){
            iter->second.first = value;
            iter->second.second = update_lru(key, iter->second.second);
            return;
        }

        if (cache.size() == cache_capacity){
            auto lru_key = lru_list.back();
            lru_list.pop_back();
            cache.erase(lru_key);
        }

        lru_list.push_front(key);
        cache[key] = make_pair(value, lru_list.begin());
        return;
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */