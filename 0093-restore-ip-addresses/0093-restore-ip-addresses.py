class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # backtracking
        # input argument: cur_str, cur_used_dots, cur_idx
        # view as search tree, in each ith level, we can chhose ith dot position and check valid part
        # height: 4 
        # time complexity o(2 ^ n) , n = len(s) 
        n = len(s)
        result = []

        def is_valid_IP(part):
            if len(part) > 1 and part[0] == "0":
                return False

            try:
                num = int(part)
                if 255 >= num and num >= 0:
                    return True

                return False

            except:
                return False

        
        def backtrack(cur_arr, cur_used_dots, cur_idx):
            if cur_used_dots == 3:
                last_part = s[cur_idx: n]

                if is_valid_IP(last_part):
                    cur_arr.append(last_part)

                    result.append(".".join(cur_arr))

                    cur_arr.pop()
                return
            
            for i in range(cur_idx + 1, n + 1):
                part = s[cur_idx: i]

                if is_valid_IP(part):

                    cur_arr.append(part)

                    backtrack(cur_arr, cur_used_dots + 1, i)

                    cur_arr.pop()
            return


        backtrack([], 0, 0)
        return result

            




