
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        compteur = {}
        for char in s: 
            compteur[char] =  compteur.get(char,0)+1
        for char in t : 
            if char not in compteur: 
                return False
            else: 
                compteur[char]-=1
            if compteur[char]<0:
                return False
        return True