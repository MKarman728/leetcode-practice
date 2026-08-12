class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        cars.sort(key=lambda x: x[0], reverse = True)
        fleets = 0
        finish = 0
        for car in cars:
            # (dis - pos) / speed = t
            pos, speed = car
            time = (target - pos) / speed 
            if time > finish:
                fleets += 1
                finish = time
        return fleets