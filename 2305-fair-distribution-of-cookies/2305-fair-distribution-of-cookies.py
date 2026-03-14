class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        # find the minimum maxmum sum of a children's cookie
        # backtrack
        #global var: mini_unfairness
        # input argument: cur_cookies_sum, cur_max_sum, cur_idx, cur_cookie_idx
        # base case: when cur_cookie_idx == len(cookies): update mini_unfair... by cur_cookie_sum and cur_max_sum
        # else:
        #  distriube the cur_cookie to chirldm from cur-idx to k
        # adn do backtrack
        mini_unfairness = float("inf")
        n = len(cookies)

        children_to_cookies = [0 for _ in range(k)]

        def backtrack(cookie_idx):
            nonlocal mini_unfairness

            if cookie_idx == n:
                mini_unfairness = min(mini_unfairness, max(children_to_cookies))
                return

            for i in range(k):
                children_to_cookies[i] += cookies[cookie_idx]

                backtrack(cookie_idx + 1)

                children_to_cookies[i] -= cookies[cookie_idx]
                
                if children_to_cookies[i] == 0:
                    break
                
        
        backtrack(0)
        return mini_unfairness
