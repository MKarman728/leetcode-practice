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
                while s[r] != s[l]:
                    cache.discard(s[l])
                    l += 1
                l += 1
        return res            