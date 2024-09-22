class MedianFinder {
private:
    priority_queue<int, vector<int>, greater<int>> min_heap;
    priority_queue<int> max_heap;
    
public:
    MedianFinder() {
    }
    
    void addNum(int num) {
        if(max_heap.empty() && min_heap.empty()){
            max_heap.push(num);
            return;
        }

        else if(min_heap.empty()){
            if(num < max_heap.top()){
                int top_val = max_heap.top();
                max_heap.pop();

                min_heap.push(top_val);
                max_heap.push(num);
            }
            else{
                min_heap.push(num);
            }
            return;
        }

        if(num <= min_heap.top() && num >= max_heap.top()){
            if(min_heap.size() > max_heap.size()){
                max_heap.push(num);
            }
            else{
                min_heap.push(num);
            }
        }

        else if (num > min_heap.top()){
            if(min_heap.size() > max_heap.size()){
                int top_val = min_heap.top();
                min_heap.pop();

                max_heap.push(top_val);
            }
            min_heap.push(num);
        }
        else{
            if(max_heap.size() > min_heap.size()){
                int top_val = max_heap.top();
                max_heap.pop();
                
                min_heap.push(top_val);
            }
            max_heap.push(num);
        }
    }
    
    double findMedian() {
        int size = max_heap.size() + min_heap.size();

        if(size % 2 == 1){
            if(min_heap.size() > max_heap.size()){
                return static_cast<double>(min_heap.top());
            }
            else{
                return static_cast<double>(max_heap.top());
            }
        }

        else{
            return (static_cast<double>(min_heap.top()) + static_cast<double>(max_heap.top())) / 2;
        }
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */