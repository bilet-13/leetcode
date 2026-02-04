class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
           # find maximum  where the capatital <= cur_capital
        # how to do that the brute force way is to build heap every picking time X
        # or just pop the capital > cur_capital and push them back after picking V

        # 1 push all (profit, capital) to maximum heap
        # 2 for loop k times:
        # each time pop the pair where capital > cur_capatil and add to list
        # pop the max_paofilt from heap and add to result_profit if no element break the loop
        # push the popped pairs back 
        # 3 finally, return the result_profit
        # time complexity o(klong(n^2))

        max_heap = [(-profits[i], capital[i]) for i in range(len(capital))]
        heapq.heapify(max_heap)
        cur_capital = w #init with w

        for _ in range(k):
            invalid_candidates = []

            while max_heap and max_heap[0][1] > cur_capital:
                invalid_candidates.append(heapq.heappop(max_heap))

            if max_heap:
                negative_profit, c = heapq.heappop(max_heap)
                cur_capital -= negative_profit
            else:
                break # no available project 
            
            for candidate in invalid_candidates:
                heapq.heappush(max_heap, candidate)
        
        return cur_capital



        
        