from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = Counter(nums)
        result= sorted(dic.items(), key = lambda x : x[1], reverse=True)
        return [num for num, _ in result[:k]]