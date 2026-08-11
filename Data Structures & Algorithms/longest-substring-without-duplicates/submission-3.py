class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cache = set()
        maxCount = 0
        l = 0
        for r in range(len(s)):
            while s[r] in cache:
                cache.remove(s[l])
                l += 1
            maxCount = max(maxCount, r - l + 1)
            cache.add(s[r])
        return maxCount