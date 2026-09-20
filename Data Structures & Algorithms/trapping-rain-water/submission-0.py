class Solution:
    def trap(self, height: List[int]) -> int:
        if not height :
            return 0
        left, right = 0, len(height)-1
        max_left =0
        max_right =0
        amount=0
        while left<right: 
            max_left = max(max_left, height[left])
            max_right = max(max_right, height[right])

            if max_left<max_right: 
                amount+= max_left - height[left]
                left+=1
            else:
                amount+= max_right -height[right]
                right -=1
        return amount
