class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if len(gas) == 1:
            return 0 if gas[0] >= cost[0] else -1
        
        if sum(gas) < sum(cost):
            return -1
        
        start = 0
        new_start = None
        visited_gas = start

        while start >= visited_gas:
            tank = 0
            for j in range(start, len(gas)):
                tank += gas[j]
                tank -= cost[j]
                if tank < 0:
                    new_start = j + 1 if j < len(gas) - 1 else 0
                    break
            if tank < 0:
                start = new_start
                visited_gas = max(visited_gas, start)
                continue
            for j in range(0, start):
                tank += gas[j]
                tank -= cost[j]
                if tank < 0:
                    new_start = j + 1 if j < len(gas) - 1 else 0
                    break
            if tank < 0:
                start = new_start
                visited_gas = max(visited_gas, start)
                continue
            else:
                return start
                
        return -1
