class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_l = [0]* 26
        s2_l = [0] * 26
        for c in s1:
            i = ord(c) - ord('a')
            s1_l[i] += 1
        l = 0
        for r, c in enumerate(s2):
            i = ord(c) - ord('a')
            s2_l[i] += 1
            if r - l + 1 > len(s1):
                l_val = ord(s2[l]) - ord('a')
                s2_l[l_val] -= 1
                l +=1
            if s1_l == s2_l:
                return True
        return False