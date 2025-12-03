class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
           # undirected graph
        # for all pair shortest path? floyd warshall
        # time complexity o(V ^ 3)
        # buidl graph o(n ^ 2)
        # return true if all pair distace != inf
        # 3 15 5
        # check the graph is connected graph or not
        # time o(n^2)
        parent = {i: i for i in range(len(nums))}
        connected_component_num = len(nums)

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            r_x = find(x)
            r_y = find(y)
            nonlocal connected_component_num

            if r_x != r_y:
                connected_component_num -= 1
                parent[r_x] = parent[r_y]

        prime_to_num = {}

        for i in range(len(nums)):
            d = 2

            temp = nums[i]
            while d * d <= nums[i]:
                if temp % d == 0:
                    if d in prime_to_num:
                        union(i, prime_to_num[d])
                    
                    else:
                        prime_to_num[d] = i
                
                while temp % d == 0:
                    temp //= d

                d += 1

            if temp > 1:
                if temp in prime_to_num:
                    union(i, prime_to_num[temp])
                
                else:
                    prime_to_num[temp] = i
        
        return connected_component_num == 1

            
        