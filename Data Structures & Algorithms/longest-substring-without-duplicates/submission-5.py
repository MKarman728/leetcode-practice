class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        cache = set()
        l = 0
        for r in range(len(s)):
            if s[r] not in cache:
                cache.add(s[r])
                res = max(res, len(cache))
            else:
                while s[r] in cache:
                    cache.discard(s[l])
                    l += 1
                cache.add(s[r])
        return res            