class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        g = defaultdict(list)
        for word in strs:
            key = tuple(sorted(word))
            g[key].append(word)
        return list(g.values())