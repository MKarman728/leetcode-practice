class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_d = Counter(s1)
        s2_d = {}
        s1_l = len(s1)
        l = 0
        for r, c in enumerate(s2):
            if r - l + 1 > s1_l:
                if s2_d[s2[l]] == 1:
                    del s2_d[s2[l]] 
                else:
                     s2_d[s2[l]] -= 1
                l += 1
            s2_d[c] = s2_d.get(c, 0) + 1
            if s2_d == s1_d:
                return True
        return False