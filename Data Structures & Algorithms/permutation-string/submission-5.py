class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s1_d = Counter(s1)
        s2_d = {}
        l = 0 
        for r in range(len(s2)):
            c = s2[r]
            if r - l + 1 > len(s1):
                lc = s2[l]
                if s2_d[lc] == 1:
                    del s2_d[lc]
                else:
                    s2_d[lc] -= 1
                l += 1
            s2_d[c] = s2_d.get(c, 0) + 1
            if s1_d == s2_d:
                return True
        return False

                