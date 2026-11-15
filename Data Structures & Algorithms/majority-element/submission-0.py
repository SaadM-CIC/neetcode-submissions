from collections import Counter
import math
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        map_ = Counter(nums)
        n = len(nums)
        for key,value in map_.items():
            if value > math.floor(n/2):
                return key
