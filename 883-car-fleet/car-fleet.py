class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), key= lambda x: x[0], reverse= True)
        
        current_time = 0
        flats = 0

        for x, v in cars:
            time = (target - x) / v
            if time > current_time:
                flats += 1
                current_time = time
        return flats