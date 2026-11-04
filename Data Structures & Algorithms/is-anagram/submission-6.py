class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        compteur = {}
        for c in s :
            compteur[c]= compteur.get(c,0)+1
        for c in t : 
            if c not in compteur : 
                return False
            else: 
                compteur[c]-=1
            if compteur[c]<0:
                return False
        return True
