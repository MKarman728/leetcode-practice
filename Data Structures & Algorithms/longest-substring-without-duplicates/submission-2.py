class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr = set()
        maxCount = 0
        l = 0
        for r in range(len(s)):
            while s[r] in curr:
                curr.remove(s[l])
                l += 1
            maxCount = max(maxCount, r - l + 1)
            curr.add(s[r])
        return maxCount