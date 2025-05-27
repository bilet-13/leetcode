class MedianFinder {
private:
    priority_queue<int> smallerHeap;
    priority_queue<int, vector<int>, greater<int>> largerHeap;
public:
    MedianFinder() {

    }
    
    void addNum(int num) {
        if (smallerHeap.size() > largerHeap.size()) {
            if (num > smallerHeap.top()) {
                largerHeap.push(num);
            } else {
                int largerNum = smallerHeap.top();
                smallerHeap.pop();

                smallerHeap.push(num);
                largerHeap.push(largerNum);
            }
        } else {
            if (largerHeap.empty() || num < largerHeap.top()) {
                smallerHeap.push(num);
            } else {
                int smallNum = largerHeap.top();
                largerHeap.pop();

                largerHeap.push(num);
                smallerHeap.push(smallNum);
            }
        }
    }
    
    double findMedian() {
        int total = smallerHeap.size() + largerHeap.size();

        if (total % 2 == 1) {
            return (double)smallerHeap.top();
        } else {
            return ((double)smallerHeap.top() + (double)largerHeap.top()) / 2;
        }
    }
};
