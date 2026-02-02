class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        min_heap = [] # element (to, numpassenger)
        cur_capacity = 0
        
        for trip in trips:
            while min_heap and min_heap[0][0] <= trip[1]:
                _, num_passengers = heapq.heappop(min_heap)
                cur_capacity -= num_passengers

            cur_capacity += trip[0]
            if cur_capacity > capacity:
                return False

            heapq.heappush(min_heap, (trip[2], trip[0]))
        
        return True
        