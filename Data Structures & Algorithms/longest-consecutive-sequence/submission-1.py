class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        for num in s : 
            if num -1 in s: 
                continue
            length =1
            while num+length in s : 
                length+=1
            
            longest = max(longest, length)

        return longest
