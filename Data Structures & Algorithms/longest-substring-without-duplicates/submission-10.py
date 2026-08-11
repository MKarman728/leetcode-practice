class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cache = set()
        l = 0
        m = 0
        for r in range(len(s)):
            if s[r] not in cache:
                cache.add(s[r])
                m = max(m, len(cache))
            else:
                while s[l] != s[r]:
                    cache.discard(s[l])
                    l += 1
                l += 1
        return m