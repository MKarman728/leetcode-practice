class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        count = set()
        l = 0
        for r in range(len(s)):
            while s[r] in count:
                count.remove(s[l])
                l+=1
            count.add(s[r])
            longest = max(longest, len(count))
        return longest
