class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for fr, to in tickets:
            graph[fr].append(to)
        for fr in graph:
            graph[fr].sort(reverse=True) # from large to samell
        
        itinerary = deque() 

        def dfs(start):
            while graph[start]:
                to = graph[start].pop()
                dfs(to)

            itinerary.appendleft(start)

        dfs("JFK")
        # itinerary.reverse()

        return list(itinerary)
            
        