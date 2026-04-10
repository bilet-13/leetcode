class Solution:
    def reorganizeString(self, s: str) -> str:
        # greedy. with max heap
        # use a max heap to store the character and number of the char
        # and a var prev taht store the prev char and count 
        # init with None and a result init with empty string
        # each time while heap not empty
        #   pop element and append it to result 
        #   push prev into heap
        #   assign prev to the cur pop elemtn and count
        #return result if len(result) == len(s) else ""

        counter = Counter(s)
        max_heap = [(-count, char) for char, count in counter.items()]
        heapq.heapify(max_heap)

        result = []
        prev = None

        while max_heap:
            neg_c, char = heapq.heappop(max_heap) 
            result.append(char)
            neg_c += 1

            if prev != None:
                heapq.heappush(max_heap, prev)
            
            prev = (neg_c, char) if neg_c < 0 else None
        
        return "".join(result) if len(result) == len(s) else ""
          
      