class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # use hash map to store the counts of 5, 10, 20 bill
        # when user give 5 count of 5 + 1
        # give 10 count of 5 - 1, 10 c + 1
        # give 20 count of 5 - 1 , 10C -1, 20 c + 1
        # return false if count <= 0 before - 1
        # in the end return true
        #o (n)

        count = defaultdict(int)
        for bill in bills:
            if bill == 5:
                count[bill] += 1
            elif bill == 10:
                if count[5] <= 0:
                    return False
                count[5] -= 1
                count[bill] += 1
            else:
                if (count[5] < 3 and count[10] <= 0) or count[5] <= 0:
                    return False
                if count[10] > 0:
                    count[5] -= 1
                    count[10] -= 1
                else:
                    count[5] -= 3
                count[bill] += 1
        
        return True


        