class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
      # pour chaque barre on va compter combien de bars sont plus grands à elle à droite et à gauche et on multiplie ce count+1 par la taille de la barre, on stocke dans une liste pour return son max.
      # si on utilise deux boucles while on aura infinity loop donc on utilise un monotonic stack pour chercher la premiere barre la plus petite à gauche et à droite et c'est ça notre condition d'arrêt
        n = len(heights)
        left =[-1]*n
        right = [n]*n
        # step 1: remplir right
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]]> heights[i]:
                j = stack.pop()
                right[j] = i
            stack.append(i)
        # step 2:  remplir left :
        for i in range(n-1,-1,-1) : 
            while stack and heights[stack[-1]]> heights[i]:
                j= stack.pop()
                left[j]=i
            stack.append(i)
        #step 3 :  calcul des aires
        best =0 
        for i in range(n):
            width = right[i]-left[i]-1
            best = max(best, heights[i]*width)
        return best




        