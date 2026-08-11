class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            k = self.convertToKey(s)
            if k not in d:
                d[k] =[]
            d[k].append(s)
        return list(d.values())

    def convertToKey(self, s):
        l = [0]*26
        for c in s:
            l[ord(c) - ord('a')] += 1
        return tuple(l)