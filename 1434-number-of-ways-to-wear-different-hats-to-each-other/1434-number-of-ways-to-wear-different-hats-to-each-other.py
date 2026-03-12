class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        # mask dp
        # mask: ith bit is 1 if ith person already wear hat
        #
        n = len(hats)
        hats_people = defaultdict(set)
        hats_num = 40

        for p in range(n):
            for hat in hats[p]:
                hats_people[hat].add(p)
       
        @cache
        def dp(hat_id, mask):
            cur_idx = mask.bit_count()

            if cur_idx == n:
                return 1

            if hat_id > hats_num:
                return 0

            ways = 0

            for p in hats_people[hat_id]:
                if mask & (1 << p) == 0 :
                    ways += dp(hat_id + 1, mask | (1 << p))

            ways = (ways + dp(hat_id + 1, mask)) % (10**9 + 7)

            return ways

        return dp(1, 0)




            
        