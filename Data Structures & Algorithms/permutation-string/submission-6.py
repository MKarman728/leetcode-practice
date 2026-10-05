class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_d = Counter(s1)
        s2_d = {}
        l, r = 0, 0
        for r in range(len(s2)):
            c = s2[r]
            if r - l + 1 > len(s1):
                lc = s2[l]
                if s2_d[lc] > 1:
                    s2_d[lc] -= 1
                else:
                    del s2_d[lc]
                l += 1
            s2_d[c] = s2_d.get(c, 0) + 1
            if s2_d == s1_d:
                return True
        return False