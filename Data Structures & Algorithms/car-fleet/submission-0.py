class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            temps=  (target- position[i])/speed[i]
            cars.append((position[i],temps))
        cars.sort(reverse=True)
        fleets =0
        max_time=0
        for pos, temps in cars:
            if temps > max_time:
                fleets+=1
                max_time=temps
        return fleets 

         
