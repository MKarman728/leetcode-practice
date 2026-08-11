class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            sr = sorted(s)
            sr = "".join(sr)
            if sr not in d:
                d[sr] = []
            d[sr].append(s)
        return list(d.values())