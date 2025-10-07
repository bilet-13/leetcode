class Solution {
public:
    string multiply(string num1, string num2) {
        if (num1 == "0" || num2 == "0") {
            return "0";
        }

        int size = num1.size() + num2.size();
        vector<int> product(size);
        string result = "";

        for (int i = num1.size() - 1; i >= 0; --i) {
            for (int j = num2.size() - 1; j >= 0; --j) {
                int mul = (num1[i] - '0') * (num2[j] - '0');
                int sum = mul + product[i + j + 1];

                product[i + j + 1] = sum % 10;
                product[i + j] += sum / 10;
            }
        }

        int start = 0;
        while (start < size && product[start] == 0) {
            start++;
        }

        for (int i = start; i < size; ++i) {
            result.push_back(product[i] + '0');
        }
        return result;
    }
};
