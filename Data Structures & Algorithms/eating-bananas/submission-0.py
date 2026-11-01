import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def heures_total(k:int) -> int:
            total = 0
            for pile in piles:
                total+= math.ceil(pile/k)
            return total
        gauche, droit = 1, max(piles)
        while gauche <droit:
            milieu = (gauche+droit)//2
            if heures_total(milieu)<=h: 
                droit = milieu
            else:
                gauche = milieu+1
        return gauche

