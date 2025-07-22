class Solution {
public:
    int numDecodings(string s) {
        //decodeDP[i]: number of way can decode substr s(from with s[0] to s[i - 1]) whcih size is i
        // 1301: 0 1201: 
        if (s[0] == '0') {
            return 0;
        }

        vector<int> decodeDP(s.size() + 1, 1);
        decodeDP[1] = 1;

        auto calculateWay = [](const char first, const char second) -> int {
            int number = (first - '0') * 10 + second - '0';
            int way = first > '0' && first < '3' && second < '7' ? 1 : 0;

            return number >= 10 && number <= 26 ? 1: 0;
        };

        for (int i = 1; i < s.size(); ++i) {
            int canCharBeMapped = s[i] != '0' ? 1 : 0;

            decodeDP[i + 1] = decodeDP[i] * canCharBeMapped + (decodeDP[i - 1] * calculateWay(s[i - 1], s[i]));

            if (decodeDP[i + 1] == 0) {
                return 0;
            }
        }
        return decodeDP[s.size()];
    }
};
