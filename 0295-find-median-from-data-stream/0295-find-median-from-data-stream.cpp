class MedianFinder {
private:
    priority_queue<int, vector<int>, greater<int>> upper_heap;
    priority_queue<int> lower_heap;
    
public:
    MedianFinder() {
    }
    
    void addNum(int num) {
        lower_heap.push(num);

        upper_heap.push(lower_heap.top());
        lower_heap.pop();
        
        if(upper_heap.size() > lower_heap.size()){
            lower_heap.push(upper_heap.top());
            upper_heap.pop();
        }
        return;
    }
    
    double findMedian() {
        int size = lower_heap.size() + upper_heap.size();

        if(size % 2 == 1){
            return static_cast<double>(lower_heap.top());
        }

        else{
            return (static_cast<double>(upper_heap.top()) + static_cast<double>(lower_heap.top())) / 2;
        }
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */