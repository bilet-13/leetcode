class Solution:
    def romanToInt(self, s: str) -> int:
        two_roman_int_pair = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, "CM": 900}
        one_roman_int_pair = {'I':1, 'V': 5, "X": 10, "L": 50, "C": 100, 'D': 500, 'M': 1000}

        start_i = 0
        sum_int = 0
        while start_i < len(s):
            if start_i+1 < len(s) and s[start_i:start_i+2] in two_roman_int_pair:
                sum_int += two_roman_int_pair[s[start_i:start_i+2]]
                start_i += 2
            else:
                sum_int += one_roman_int_pair[s[start_i]]
                start_i += 1
        return sum_int