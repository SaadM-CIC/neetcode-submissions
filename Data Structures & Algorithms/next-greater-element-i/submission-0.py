class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack =[]
        greater = {}
        for x in nums2: 
            while stack and x>stack[-1]:
                previous=stack.pop()
                greater[previous]= x
            stack.append(x)
        while stack: 
            greater[stack.pop()]=-1
        ans=[]
        for x in nums1:
            ans.append(greater[x])
        return ans