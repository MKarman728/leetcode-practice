class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cache = set()
        max_count = 0
        l = 0
        for r in range(len(s)):
            if s[r] not in cache:
                cache.add(s[r])
                max_count = max(max_count, r - l + 1)
            else:
                while s[l] != s[r]:
                    cache.discard(s[l])
                    l += 1
                l +=1
        return max_count