class MedianFinder {
private:
    vector<int> sorted_nums;
public:
    MedianFinder() {
    }
    
    void addNum(int num) {
        int left = 0;
        int right = sorted_nums.size()-1;
        int len = sorted_nums.size();

        while(left <= right){
            int mid = left + (right-left) / 2;

            if(sorted_nums[mid] == num){
                sorted_nums.insert(sorted_nums.begin()+mid, num);
                break;
            }
            else if(sorted_nums[mid] > num){
                right = mid-1;
            }
            else{
                left = mid+1;
            }
        }

        if(sorted_nums.size() == len){
            sorted_nums.insert(sorted_nums.begin()+left, num);
        }

    }
    
    double findMedian() {
        double result = 0.0;

        if(sorted_nums.size() % 2 == 1){
            int middle = sorted_nums.size() / 2;
            return static_cast<double>(sorted_nums[middle]);
        }
        else{
            int middle = sorted_nums.size() / 2;
            double num1 = sorted_nums[middle];
            double num2 = sorted_nums[middle-1];
            return (num1 + num2) / 2;
        }
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */