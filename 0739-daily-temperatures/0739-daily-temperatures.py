class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        warmer_temperatures = deque()
        result = [0 for _ in range(len(temperatures))]
        
        for i in range(len(temperatures) - 1, -1, -1):
            while warmer_temperatures and temperatures[i] >= warmer_temperatures[-1][0]:
                warmer_temperatures.pop()

            if warmer_temperatures and temperatures[i] < warmer_temperatures[-1][0]:
                result[i] = warmer_temperatures[-1][1] - i
            
            warmer_temperatures.append((temperatures[i], i))

        return result

