class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # use hash map to store the counts of 5, 10, 20 bill
        # when user give 5 count of 5 + 1
        # give 10 count of 5 - 1, 10 c + 1
        # give 20 count of 5 - 1 , 10C -1, 20 c + 1
        # return false if count <= 0 before - 1
        # in the end return true
        #o (n)
        five = 0
        ten = 0
        count = defaultdict(int)
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five <= 0:
                    return False
                five -= 1
                ten += 1
            else:
                if five > 0 and ten > 0:
                    five -= 1
                    ten -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        
        return True


        