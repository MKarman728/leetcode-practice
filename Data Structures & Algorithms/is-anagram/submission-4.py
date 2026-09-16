class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = [0]*26
        t_list = [0]*26
        for l in s:
            s_list[ord(l) - ord('a')] += 1
        for l in t:
            t_list[ord(l)- ord('a')] += 1
        return s_list == t_list