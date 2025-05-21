class Solution {
private:
    static double calculateDistance(const vector<int> &point) {
        return point[0] * point[0] + point[1] * point[1];
    }

public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        auto cmp = [](const vector<int> &a, const vector<int> &b) {
            return calculateDistance(a) < calculateDistance(b);
        };
        // size k min heap
        priority_queue<vector<int>, vector<vector<int>>, decltype(cmp)> maxHeap(cmp);

        // for num if num <= heap.top do nothing else heap.pop() heap.push(num)
        for (vector<int> point : points) {
            int distance = calculateDistance(point);

            if (maxHeap.size() < k) {
                maxHeap.push(point);
            } else {
                if (calculateDistance(maxHeap.top()) > distance) {
                    maxHeap.pop();
                    maxHeap.push(point);
                }
            }
        }

        // return vecor of nums in heap
        vector<vector<int>> result;
        while( !maxHeap.empty()) {
            result.push_back(maxHeap.top());
            maxHeap.pop();
        }
        
        return result;
    }
};
