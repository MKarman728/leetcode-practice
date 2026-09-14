class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l= 0
        d = {}
        m = 0
        for r in range(len(s)):
            d[s[r]] = d.get(s[r], 0) + 1
            while r - l + 1 - max(d.values()) > k:
                d[s[l]] -= 1
                l += 1
            m = max(m, r - l + 1)
        return m