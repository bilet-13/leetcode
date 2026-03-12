class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        # backtracking
        # argument, cur_way, cur_idx(cur_idx person now)
        # global set : used_hats
        used_hats = set()
        result = 0
        n = len(hats)

        def backtrack(cur_idx, cur_way):
            nonlocal result

            if cur_idx == n:
                result = (result + 1) % (10**9 + 7)
                return

            for hat in hats[cur_idx]:
                if hat not in used_hats:
                    used_hats.add(hat)
                    backtrack(cur_idx + 1, cur_way)
                    used_hats.remove(hat)
            return

        backtrack(0, 0)
        return result
                



            
        