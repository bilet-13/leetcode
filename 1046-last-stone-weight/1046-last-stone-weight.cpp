class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int> maxHeap(stones.begin(), stones.end());

        while (maxHeap.size() > 1) {
            int largestStone = maxHeap.top();
            maxHeap.pop();
            int secondLargestStone = maxHeap.top();
            maxHeap.pop();

            int remainStone = largestStone - secondLargestStone;

            if (remainStone > 0) {
                maxHeap.push(remainStone);
            }
        }

        return maxHeap.empty() ? 0 : maxHeap.top();
    }
};
