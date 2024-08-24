class LRUCache {
public:
    LRUCache(int capacity) : capacity(capacity) {}

    int get(int key) {
        if (cache.find(key) == cache.end()) {
            return -1; // Key not found
        }
        // Key found, move it to the front of the list
        updateLRU(key);
        return cache[key].first;
    }

    void put(int key, int value) {
        if (cache.find(key) != cache.end()) {
            // Key exists, update the value and move it to the front
            cache[key].first = value;
            updateLRU(key);
        } else {
            // Key doesn't exist, insert it
            if (lruList.size() == capacity) {
                // Cache is full, remove the least recently used item
                int lru_key = lruList.back();
                lruList.pop_back();
                cache.erase(lru_key);
            }
            lruList.push_front(key);
            cache[key] = {value, lruList.begin()};
        }
    }

private:
    int capacity;
    list<int> lruList; // Stores keys in LRU order
    unordered_map<int, pair<int, list<int>::iterator>> cache; // Maps key to (value, list iterator)

    void updateLRU(int key) {
        // Move the accessed key to the front of the list
        lruList.erase(cache[key].second);
        lruList.push_front(key);
        cache[key].second = lruList.begin();
    }
};