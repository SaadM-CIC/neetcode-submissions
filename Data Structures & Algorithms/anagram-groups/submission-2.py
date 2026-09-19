from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        anagram_map = defaultdict(list)
        for s in strs: 
            sorted_s= tuple(sorted(s))
            anagram_map[sorted_s].append(s)
        for value in anagram_map.values():
            result.append(value)
        return result
        