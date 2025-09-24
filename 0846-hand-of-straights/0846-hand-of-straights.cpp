class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {
        int n = hand.size();
        unordered_map<int, int> frequencies;

        if ((n % groupSize) != 0) {
            return false;
        }

        sort(hand.begin(), hand.end()); // nlogn

        for (const auto& num: hand) {
            frequencies[num] += 1;
        }

        for (int i = 0; i < n; ++i) {
            if (frequencies.count(hand[i]) && frequencies[hand[i]] != 0) {
                int num = hand[i];
                frequencies[num]--;

                for (int j = 1; j < groupSize; ++j) {
                    num++;
                    if (!frequencies.count(num) || frequencies[num] == 0) {
                        return false;
                    }
                    frequencies[num]--;
                }
            }
        } // o(n)

        return true;// o(nlogn)
    }
};
