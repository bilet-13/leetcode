class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), key=lambda x: x[0])
        car_fleet = deque()

        for pos, speed in reversed(cars):
            time = (target - pos) / speed

            if not car_fleet or car_fleet[-1] < time:
                car_fleet.append(time)
        
        return len(car_fleet)